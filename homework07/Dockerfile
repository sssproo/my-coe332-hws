FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y curl iproute2 net-tools && \
    apt-get clean

WORKDIR /app

COPY requirements.txt .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "gene_api.py"]
