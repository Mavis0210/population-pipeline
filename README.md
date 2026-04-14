# Population Data Pipeline

## Overview
End-to-end ETL pipeline that extracts world population data, transforms it with Python, and loads it into PostgreSQL, orchestrated with Kestra and containerised with Docker.

## Pipeline Architecture
GitHub CSV → Extract → Transform (Python) → Load → PostgreSQL


## Tech Stack
- **Kestra** - workflow orchestration
- **Python** (Pandas, SQLAlchemy) - data transformation
- **PostgreSQL** - data storage
- **Docker & Docker Compose** - containerisation

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
1. Clone the repo
git clone https://github.com/Mavis0210/population-pipeline.git
cd population-pipeline

2. Create your environment file
cp .env.example .env

3. Start services
docker compose up -d

### Access
| Service | URL |
|---------|-----|
| Kestra UI | http://localhost:8082 |
| pgAdmin | http://localhost:8084 |

### Run Pipeline
1. Open Kestra UI at http://localhost:8082
2. Navigate to population_pipeline flow
3. Click Execute
4. Verify data in pgAdmin at http://localhost:8084

### Project Structure
```
population-pipeline/
├── docker-compose.yaml        # All services
├── Dockerfile                 # Custom image config
├── population_pipeline.yaml   # Kestra flow definition
├── ingest_population.py       # Standalone ingestion script
├── requirements.txt           # Python dependencies
└── README.md
```
