# Homework 08 - Holidapp

In this homework, we will extend our Flask API and Redis DB application to include dynamic Redis client host IP assignment and image storage in the Redis database. We assume that you have already completed Homework 06 and Homework 07, and have a working application with Kubernetes deployment files.

## Prerequisites

- A working Flask API and Redis DB application from Homework 06 and Homework 07
- Docker installed and configured
- Access to a Kubernetes cluster
- kubectl installed and configured
- A Docker Hub account

## Getting Started

1. Clone the repository and navigate to the `homework08` directory.

```
git clone <git-repo-url>
cd my-coe332-hws/homework08
```

1. Make sure your Docker image for the Flask app is up-to-date and pushed to Docker Hub.

```
docker build -t ssspro/hw08:latest .
docker push ssspro/hw08:latest
```


## Deploying the Application to Kubernetes

1. Create the necessary Kubernetes objects using the configuration files provided:

```
phpCopy codecd kubernetes
kubectl apply -f kubernetes/ssspro-test-redis-pvc.yml
kubectl apply -f kubernetes/ssspro-test-redis-deployment.yml
kubectl apply -f kubernetes/ssspro-test-redis-service.yml
kubectl apply -f kubernetes/ssspro-test-flask-deployment.yml
kubectl apply -f kubernetes/ssspro-test-flask-service.yml
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


## Testing the /image Route

1. Create a simple plot of the data by making a POST request to the /image route:

```
curl -X POST http://<flask-service-ip>:5000/image
```

2. Retrieve the image from the database (db=1) by making a GET request to the /image route:

```
curl -X GET http://<flask-service-ip>:5000/image --output my-image.png
```

3. Delete the image from the database by making a DELETE request to the /image route:

```
curl -X DELETE http://<flask-service-ip>:5000/image
```

## Cleaning Up

To clean up the resources created, run the following commands:

```
kubectl delete -f kubernetes/ssspro-test-flask-service.yml
kubectl delete -f kubernetes/ssspro-test-flask-deployment.yml
kubectl delete -f kubernetes/ssspro-test-redis-service.yml
kubectl delete -f kubernetes/ssspro-test-redis-deployment.yml
kubectl delete -f kubernetes/ssspro-test-redis-pvc.yml
```

## Data Description

The HGNC dataset contains information about human genes, such as gene names, symbols, and gene groups. It is in a list-of-dictionaries format with 54 fields, some of which are sparsely populated. The dataset is provided by the [Human Genome Organization](https://www.genenames.org/), a non-profit organization that oversees the HGNC.

For more information on the dataset and its fields, please refer to the [HGNC documentation](https://www.genenames.org/download/archive/).

### Data Citation

HUGO Gene Nomenclature Committee. (2021). *HGNC Database, version 2021.09*. Retrieved from https://www.genenames.org/download/archive/