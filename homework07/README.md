# Homework 07

In this homework, we'll deploy the Flask API and Redis database from Homework 06 onto a Kubernetes cluster. This provides stability and allows our application to be easily exposed to the rest of the world.
## Prerequisites

- Docker
- Kubernetes cluster access
- `kubectl` CLI tool
- A Docker Hub account

## Project Structure

```
graphqlCopy codehomework07/
│
├── app.py               # Flask API script
├── Dockerfile           # Dockerfile for containerizing the Flask app
├── requirements.txt     # Python dependencies for the Flask app
│
├── k8s/                 # Kubernetes YAML configuration files
│   ├── pvc.yaml
│   ├── redis-deployment.yaml
│   ├── redis-service.yaml
│   ├── flask-deployment.yaml
│   └── flask-service.yaml
│
└── README.md            # This README file
```

## Setup

1. Clone the repository and navigate to the `homework07` directory.
2. Make sure you have access to a Kubernetes cluster and have the `kubectl` CLI tool installed.

## Building the Docker Image

### Option 1: Using the existing image from Docker Hub


```
docker pull ssspro/hw07:latest
```

### Option 2: Building a new image from the Dockerfile

Run the following command in the `homework07` directory:

```
docker build -t ssspro/hw07:latest .
```

Then, push the image to your Docker Hub repository:

```
docker push ssspro/hw07:latest
```

## Deploying to Kubernetes

1. Apply the Kubernetes configurations:

```
kubectl apply -f ssspro-test-redis-pvc.yml
kubectl apply -f ssspro-test-redis-deployment.yml
kubectl apply -f ssspro-test-redis-service.yml
kubectl apply -f ssspro-test-flask-deployment.yml
kubectl apply -f ssspro-test-flask-service.yml
kubectl apply -f deployment-flask-debug.yml
```

2. Verify that the resources have been created:

```
kubectl get all
```
3. Find the FLASK_POD_NAME for the Flask service:

```
kubectl get pods
```
Take note of the `NAME` for the `ssspro-test-flask`.


4. Find the ClusterIP for the Flask service:

```
kubectl get services
```

Take note of the `CLUSTER-IP` for the `ssspro-test-flask`.


5. Test the API using `curl`:

```
kubectl exec -it FLASK_POD_NAME  -- /bin/bash
curl -X POST http://<CLUSTER-IP>:5000/data
curl http://<CLUSTER-IP>:5000/genes
curl http://<CLUSTER-IP>:5000/genes/HGNC:5
```

Replace `<CLUSTER-IP>` with the IP address you found in step 4.

## Cleaning Up

To delete the deployed resources:

```
kubectl delete -f ssspro-test-redis-pvc.yml
kubectl delete -f ssspro-test-redis-deployment.yml
kubectl delete -f ssspro-test-redis-service.yml
kubectl delete -f ssspro-test-flask-deployment.yml
kubectl delete -f ssspro-test-flask-service.yml
```

## Data Description

The HGNC dataset contains information about human genes, such as gene names, symbols, and gene groups. It is in a list-of-dictionaries format with 54 fields, some of which are sparsely populated. The dataset is provided by the [Human Genome Organization](https://www.genenames.org/), a non-profit organization that oversees the HGNC.

For more information on the dataset and its fields, please refer to the [HGNC documentation](https://www.genenames.org/download/archive/).

### Data Citation

HUGO Gene Nomenclature Committee. (2021). *HGNC Database, version 2021.09*. Retrieved from https://www.genenames.org/download/archive/