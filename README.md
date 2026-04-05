AgentLoopGen

AgentLoopGen is a production-ready background job execution framework designed to run asynchronous tasks reliably using workers, queues, retries, and status tracking.

It provides the infrastructure layer that powers applications like RouteIQ, ensuring workflows continue running even under failures, restarts, or high load.

---

Overview

AgentLoopGen separates task execution from API requests, improving system performance, reliability, and scalability.

Typical workflow:

Client → API → Database → Worker → Execution → Status Update

---

Core Features

- Background job queue
- Worker execution engine
- Automatic retry logic
- Job status tracking
- Health monitoring endpoints
- PostgreSQL integration
- Docker-ready deployment
- Production-safe architecture

---

Use Cases

- Route processing
- Delivery scheduling
- Email / SMS notifications
- Data processing
- Report generation
- Workflow automation
- Background task execution

---

Architecture

Client / Dashboard
        ↓
FastAPI API
        ↓
PostgreSQL Database
        ↓
Worker Process
        ↓
Retry + Status Tracking

---

Project Structure

survival-project/
└── routeiq/
    └── backend/
        ├── main.py
        ├── worker.py
        ├── database.py
        ├── config.py
        ├── requirements.txt
        ├── Dockerfile
        └── docker-compose.yml

---

Installation

Clone Repository

git clone https://github.com/Anuragkumarbhot/agentloopgen.git
cd survival-project/routeiq/backend

Install Dependencies

pip install -r requirements.txt

---

Environment Variables

Create a ".env" file:

DATABASE_URL=postgresql://USER:PASSWORD@HOST:PORT/DATABASE
REDIS_URL=redis://your-redis-url
ENV=production

---

Running Locally

Start API

uvicorn main:app --host 0.0.0.0 --port 8000

Start Worker

python worker.py

---

Running with Docker

Build and start services:

docker compose up --build

Services started:

- API server
- Worker process

---

API Endpoints

Health Check

GET /health

Response:

{
  "status": "ok"
}

---

Database Health

GET /db-health

---

Create Job

POST /jobs

---

Get Jobs

GET /jobs

---

Job Lifecycle

pending
   ↓
processing
   ↓
completed
   ↓
failed
   ↓
retrying

---

Worker Responsibilities

- Poll database for pending jobs
- Execute tasks
- Handle failures
- Retry automatically
- Update job status
- Log execution results

---

Deployment

AgentLoopGen is designed for production deployment on:

- Render
- Docker
- Kubernetes
- Cloud platforms
- On-premise servers

---

Reliability Features

- Automatic retries
- Failure isolation
- Idempotent execution
- Health monitoring
- Stateless workers
- Persistent job storage

---

Scaling

Horizontal scaling is supported by running multiple workers:

Worker 1
Worker 2
Worker 3
Worker N

All workers consume jobs from the same queue safely.

---

Roadmap

- React monitoring dashboard
- Scheduled jobs (cron)
- Rate limiting
- Priority queues
- Distributed workers
- Metrics and observability
- Multi-tenant support

---

License

MIT License

---

Maintainer

Anurag Kumar

---

Tagline

Reliable background job execution for production systems.
