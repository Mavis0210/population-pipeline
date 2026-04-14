FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ingest_population.py .

ENTRYPOINT ["python", "ingest_population.py"]