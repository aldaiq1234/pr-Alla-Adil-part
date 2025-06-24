# Logistic.ai — Intelligent Logistics Monitoring Platform

**Logistic.ai** is a backend platform for monitoring vehicle operations, analyzing logistics routes, and predicting fuel consumption using machine learning. The system was developed as part of an internship project by students of the Computer Science program at AITU (2025).

## Technology Stack

- **FastAPI** – RESTful API development
- **PostgreSQL** – Data storage
- **SQLAlchemy** – ORM integration
- **Scikit-learn / XGBoost** – Machine learning models
- **OpenWeather API** – Weather data integration
- **Wialon SDK (mock)** – Simulated vehicle telemetry
- **Docker / Docker Compose** – Containerization and deployment

## Features

- Data management for routes, vehicles, and fuel logs
- Fuel consumption prediction based on distance, speed, temperature, and cargo weight
- Weather data retrieval by city using OpenWeather API
- Simulated integration with Wialon for telemetry data
- Bearer token-based authentication
- Dockerized deployment environment

## Project Structure

.
├── app/ # Backend application
│ ├── api/ # Routers (predict, weather, wialon)
│ ├── models/ # ORM models
│ ├── core/ # Database and configuration
│ ├── ml/ # Trained ML model (.pkl)
│ └── main.py # FastAPI entry point
├── notebooks/ # Colab notebook for ML training
├── .env.example # Environment configuration template
├── Dockerfile
├── docker-compose.yml
└── README.md

bash
Копировать
Редактировать

## Getting Started (Docker)

1. Clone the repository:

```bash
git clone https://github.com/yourusername/logistic-ai.git
cd logistic-ai
Copy the environment file and configure your variables:

bash
Копировать
Редактировать
cp .env.example .env
Build and run the application:

bash
Копировать
Редактировать
docker-compose up --build
The API will be available at http://localhost:8000

Machine Learning
The /notebooks directory includes a Google Colab notebook that contains the complete ML pipeline:

Data processing (fuel_logs, routes, vehicles)

Feature engineering (avg_speed, weight, temperature)

Model training and comparison (Linear Regression, Random Forest, XGBoost)

Export of the best model as .pkl

Environment Variables
Example .env configuration:

env
Копировать
Редактировать
DATABASE_URL=postgresql://user:password@db:5432/logistic_db
OPENWEATHER_API_KEY=your_openweather_key
SECRET_KEY=your_jwt_secret
API Endpoints
POST /predict – Predict fuel consumption

GET /weather?city=Astana – Get weather by city

GET /wialon/{vehicle_id} – Simulated telemetry data

GET / – API status check
