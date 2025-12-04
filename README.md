# 🐍 FastAPI Backend — Campaign Analytics API

A simple backend service that exposes a `/campaigns` endpoint to return marketing campaign data stored in a PostgreSQL database.  
Built using **FastAPI**, **Pipenv**, and **PostgreSQL**, as required in the assignment.

## 🚀 Features

- FastAPI-based REST API
- PostgreSQL database integration
- `/campaigns` endpoint returning 10 sample records
- Pydantic models and schema validation
- CORS enabled for frontend access
- Pipenv for environment and dependency management

## 📦 Tech Stack

- **FastAPI**
- **Uvicorn**
- **SQLAlchemy**
- **Pydantic**
- **Pipenv**
- **PostgreSQL**

## 🛠️ Setup Instructions

### Clone the Repository

```
git clone https://github.com/Jigar-Gadhia/campaign-analytics-dashboard-server.git
```
```
cd campaign-analytics-dashboard-server
```
Make sure python and pip are installed before running below command
```
pip install pipenv
```
```
pipenv install
```
Activate pipenv
```
pipenv shell
```

## ⚙️ Environment Variables

Create a `.env` file in the backend root with the following variable:

```
DATABASE_URL=postgresql://username:password@localhost:5432/DBname
```

## 🌱 Seed Database (Sample Data)

To insert the sample campaign data into the database, run the seed script located in `seed/seed.py`.

Make sure your virtual environment is active, then run:

```
pipenv run python seed/seed.py
```

## 📡 API Endpoints

### `GET /campaigns`

Returns a list of campaigns stored in the database.  
Supports optional filtering by status.

---

### 📥 Query Parameters

| Name   | Type                  | Required | Description                         |
|--------|-----------------------|----------|-------------------------------------|
| status | `"Active" "Paused"`   | No       | Filter campaigns by status value    |

---

### 🔍 Example Request

**Get all campaigns**

```
GET /campaigns
```

### 🔍 Filter Examples

**Get only active campaigns**

```
GET /campaigns?status=Active
```

**Get only pause campaigns**

```
GET /campaigns?status=Pause
```

