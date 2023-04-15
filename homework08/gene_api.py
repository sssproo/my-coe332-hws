import os
import sys
from typing import Any
from flask import Flask, request, jsonify, g, Response
import requests
import redis
import json
import csv
from io import StringIO, BytesIO
import base64
from PIL import Image
import matplotlib.pyplot as plt



app = Flask(__name__)
# r = redis.StrictRedis()

HGNC_URL = "https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/tsv/hgnc_complete_set.txt"
redis_host = os.environ.get('REDIS_IP')
redis_port = 6379

if not redis_host:
    raise Exception("REDIS_IP environment variable not set")

def get_redis():
    if "redis" not in g:
        g.redis = redis.Redis(host=redis_host, port=redis_port, db=0)
        g.rd_images = redis.Redis(host=redis_host, port=redis_port, db=1)
    return g.redis, g.rd_images


@app.before_request
def before_request() -> None:
    g.redis, g.rd_images = get_redis()


@app.teardown_request
def teardown_request(exception: Any) -> None:
    rd_connection = g.pop("redis", None)
    if rd_connection is not None:
        rd_connection.close()
    rd_images_connection = g.pop("rd_images", None)
    if rd_images_connection is not None:
        rd_images_connection.close()

def download_with_progress(url: str) -> str:
    response = requests.get(url, stream=True)
    response.raise_for_status()

    total_size = int(response.headers.get("content-length", 0))
    downloaded_size = 0

    chunks = []
    for chunk in response.iter_content(chunk_size=1024):
        downloaded_size += len(chunk)
        chunks.append(chunk)
        progress_percent = (downloaded_size / total_size) * 100
        sys.stdout.write(f"\rDownloading: {progress_percent:.2f}%")
        sys.stdout.flush()

    sys.stdout.write("\n")
    return b"".join(chunks).decode()

def load_data_to_redis() -> None:
    """
    Fetches HGNC data from the web and stores it in the Redis database as a hash.
    """

    try:
        response_text = download_with_progress(HGNC_URL)
    except requests.RequestException as e:
        raise RuntimeError("Error fetching HGNC data: {}".format(e))
    tsv_file = StringIO(response_text)
    reader = csv.DictReader(tsv_file, delimiter="\t")

    for row in reader:
        g.redis.hset("hgnc_data", row["hgnc_id"], json.dumps(row))


@app.route("/data", methods=["POST", "GET", "DELETE"])
def data_route() -> Any:
    if request.method == "POST":
        try:
            load_data_to_redis()
            return jsonify({"message": "Data loaded to Redis"}), 200
        except RuntimeError as e:
            return jsonify({"error": str(e)}), 500
    elif request.method == "GET":
        data = [json.loads(v) for v in g.redis.hvals("hgnc_data")]
        return jsonify(data), 200
    elif request.method == "DELETE":
        g.redis.delete("hgnc_data")
        return jsonify({"message": "Data deleted from Redis"}), 200


@app.route("/genes", methods=["GET"])
def genes_route() -> Any:
    hgnc_ids = [k.decode() for k in g.redis.hkeys("hgnc_data")]
    return jsonify(hgnc_ids), 200


@app.route("/genes/<string:hgnc_id>", methods=["GET"])
def gene_by_id_route(hgnc_id: str) -> Any:
    data = g.redis.hget("hgnc_data", hgnc_id)
    if data is None:
        return jsonify({"message": "Gene not found"}), 404

    gene_data = json.loads(data)
    return jsonify(gene_data), 200

@app.route('/image', methods=['POST', 'GET', 'DELETE'])
def image():
    if request.method == 'POST':
        # Read some portion of data from the database (db=0)
        data = [k.decode() for k in g.redis.hkeys("hgnc_data")]
        if not data:
            return jsonify({"error": "No data found in the database"}), 400

        # Create a simple plot using matplotlib
        plt.plot(data)

        # Save the plot to a BytesIO buffer
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        # Encode the image as base64 and store it in the database (db=1)
        image_data = base64.b64encode(buf.getvalue()).decode()
        g.rd_images.set('plot_image', image_data)

        return jsonify({"message": "Image created and stored successfully"}), 200

    elif request.method == 'GET':
        # Check if the image is present in the database
        image_data = g.rd_images.get('plot_image')
        if not image_data:
            return jsonify({"error": "No image found in the database"}), 404

        # Decode the base64 image and return it
        img = base64.b64decode(image_data)
        response = Response(img, content_type="image/png")
        return response

    elif request.method == 'DELETE':
        # Delete the image from the database if it exists
        if g.rd_images.get('plot_image'):
            g.rd_images.delete('plot_image')
            return jsonify({"message": "Image deleted successfully"}), 200
        else:
            return jsonify({"error": "No image found in the database"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

