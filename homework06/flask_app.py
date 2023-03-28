from typing import Any
from flask import Flask, request, jsonify
import requests
import redis
import json
import csv
from io import StringIO


app = Flask(__name__)
r = redis.StrictRedis()

HGNC_URL = "https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/tsv/hgnc_complete_set.txt"


def load_data_to_redis() -> None:
    """
    Fetches HGNC data from the web and stores it in the Redis database as a hash.
    """

    try:
        response = requests.get(HGNC_URL)
        response.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError("Error fetching HGNC data: {}".format(e))
    response_text = response.text
    tsv_file = StringIO(response_text)
    reader = csv.DictReader(tsv_file, delimiter="\t")

    for row in reader:
        r.hset("hgnc_data", row["hgnc_id"], json.dumps(row))


@app.route("/data", methods=["POST", "GET", "DELETE"])
def data_route() -> Any:
    if request.method == "POST":
        try:
            load_data_to_redis()
            return jsonify({"message": "Data loaded to Redis"}), 200
        except RuntimeError as e:
            return jsonify({"error": str(e)}), 500
    elif request.method == "GET":
        data = [json.loads(v) for v in r.hvals("hgnc_data")]
        return jsonify(data), 200
    elif request.method == "DELETE":
        r.delete("hgnc_data")
        return jsonify({"message": "Data deleted from Redis"}), 200


@app.route("/genes", methods=["GET"])
def genes_route() -> Any:
    hgnc_ids = [k.decode() for k in r.hkeys("hgnc_data")]
    return jsonify(hgnc_ids), 200


@app.route("/genes/<string:hgnc_id>", methods=["GET"])
def gene_by_id_route(hgnc_id: str) -> Any:
    data = r.hget("hgnc_data", hgnc_id)
    if data is None:
        return jsonify({"message": "Gene not found"}), 404

    gene_data = json.loads(data)
    return jsonify(gene_data), 200


if __name__ == "__main__":
    app.run(debug=True)

