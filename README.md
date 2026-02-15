# Backend Reporting System

A containerized backend reporting system built using FastAPI, PostgreSQL, and TimescaleDB for scalable time-series data ingestion and reporting via REST APIs.

---

## Overview

This project implements a production-style backend architecture designed to:

- Ingest time-series data via CSV and JSON APIs
- Store structured metrics using TimescaleDB hypertables
- Provide RESTful endpoints for querying and reporting
- Run in isolated containers using Docker Compose

The system demonstrates backend development, database modeling, containerization, and API design principles.

---

## Architecture

FastAPI (Backend API)
        ↓
SQLAlchemy ORM
        ↓
PostgreSQL + TimescaleDB (Hypertables)
        ↓
Dockerized Deployment

---

## Key Features

- REST API endpoints for metric ingestion
- CSV upload-based data ingestion
- JSON-based API ingestion
- Time-series storage using TimescaleDB hypertables
- Containerized backend and database setup
- Automatic table creation via ORM models
- Swagger UI documentation

---

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- TimescaleDB
- Docker & Docker Compose

---

## Database Design

The `metrics` table uses a composite primary key and is converted into a TimescaleDB hypertable for efficient time-series storage.

Columns include:
- time (timestamp)
- ava_id
- metric_name
- value
- unit
- extra_data (JSON)

---

## Running the Project

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/backend-reporting-system.git
cd backend-reporting-system
