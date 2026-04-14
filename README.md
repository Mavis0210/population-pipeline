# Population Data Pipeline

## Overview
End-to-end ETL pipeline that extracts world population data, transforms it with Python, and loads it into PostgreSQL, orchestrated with Kestra and containerised with Docker.

## Pipeline Architecture
GitHub CSV → Extract → Transform (Python) → Load → PostgreSQL


## Tech Stack
- **Kestra** — workflow orchestration
- **Python** (Pandas, SQLAlchemy) — data transformation
- **PostgreSQL** — data storage
- **Docker & Docker Compose** — containerisation

## Pipeline Tasks
| Task | Description |
|------|-------------|
| `extract` | Downloads world population CSV from GitHub |
| `transform` | Cleans data — fixes column names, drops nulls, removes duplicates |
| `load` | Loads cleaned data into PostgreSQL |
| `done` | Confirms pipeline completion |

## Key Concepts Demonstrated
- Workflow orchestration with Kestra (YAML)
- Docker bridge networking for container-to-container communication
- Scheduled triggers (every Monday at 9am)
- Data transformation with Pandas
- Loading data into PostgreSQL with SQLAlchemy

## How To Run

### Prerequisites
- Docker & Docker Compose installed

### Setup
```bash
# Clone the repo
git clone https://github.com/Mavis0210/population-pipeline.git
cd population-pipeline

# Create .env file
cp .env.example .env

# Start services
docker compose up -d
Access
Service	URL
Kestra UI	http://localhost:8082
pgAdmin	http://localhost:8084
Run Pipeline
Open Kestra UI at http://localhost:8082
Navigate to population_pipeline flow
Click Execute
Verify data in pgAdmin at http://localhost:8084
Project Structure

population-pipeline/
├── docker-compose.yaml        # All services
├── Dockerfile                 # Custom image config
├── population_pipeline.yaml   # Kestra flow definition
├── ingest_population.py       # Standalone ingestion script
├── requirements.txt           # Python dependencies
└── README.md
