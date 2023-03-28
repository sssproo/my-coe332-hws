import requests

# Replace 'localhost' with the IP of the Docker container if you're running the Flask app in Docker
base_url = "http://localhost:5000"

# Test POST /data
response = requests.post(base_url + "/data")
print("POST /data status code:", response.status_code)
print("POST /data response text:", response.text)

# Test GET /data
response = requests.get(base_url + "/data")
print("GET /data:", response.json())

# Test GET /genes
response = requests.get(base_url + "/genes")
print("GET /genes:", response.json())

# Test GET /genes/<hgnc_id> with a valid hgnc_id
valid_hgnc_id = "HGNC:50799"  # Replace with an actual hgnc_id from the dataset
response = requests.get(base_url + f"/genes/{valid_hgnc_id}")
print(f"GET /genes/{valid_hgnc_id}:", response.json())

# Test GET /genes/<hgnc_id> with an invalid hgnc_id
invalid_hgnc_id = "invalid"
response = requests.get(base_url + f"/genes/{invalid_hgnc_id}")
print(f"GET /genes/{invalid_hgnc_id}:", response.json())

# Test DELETE /data
response = requests.delete(base_url + "/data")
print("DELETE /data:", response.json())
