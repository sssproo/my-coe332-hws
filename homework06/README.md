# Flask-HGNC-Gene-Data

A Flask web application for fetching, storing, and retrieving HGNC gene data using Redis as a database.

## Contents

- `app.py`: The main Flask application file.
- `Dockerfile`: The Dockerfile for building the Flask application container.
- `docker-compose.yml`: The Docker Compose file for orchestrating the Flask app and Redis services.
- `requirements.txt`: The list of required Python packages for the Flask application.

## Getting Started

### Using the pre-built Docker image

1. Install [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/).
2. Run `docker-compose up` from the root directory of the project.
3. Access the application at `http://localhost:5000`.

### Building your own Docker image

1. Install [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/).
2. Run `docker build -t your-image-name .` from the root directory of the project.
3. Update the `docker-compose.yml` file to use your custom image for the `app` service:

   ```yaml
   app:
     image: your-image-name
     ports:
       - "5000:5000"
     depends_on:
       - redis
4. Run docker-compose up from the root directory of the project.
5. Access the application at http://localhost:5000.