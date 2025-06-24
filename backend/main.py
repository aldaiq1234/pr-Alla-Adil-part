import os
import logging
import time
from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from dotenv import load_dotenv
from sqlalchemy import text

from database import engine, SessionLocal, Base
from api import predict, weather, wialon


load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("logistic-ai")


app = FastAPI(
    title="Logistic.ai API",
    version="1.0.0",
    description="AI-платформа логистики с интеграцией Wialon, погодой и аналитикой топлива.",
    license_info={"name": "MIT", "url": "https://opensource.org/licenses/MIT"}
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time
        logger.info(f"{request.method} {request.url} [{response.status_code}] in {duration:.3f}s")
        return response

app.add_middleware(LoggingMiddleware)


@app.on_event("startup")
async def startup():
    logger.info("Starting Logistic")
    Base.metadata.create_all(bind=engine)

@app.on_event("shutdown")
async def shutdown():
    logger.info("Stopping Logistic")


@app.exception_handler(StarletteHTTPException)
async def http_error_handler(request, exc):
    logger.warning(f"HTTP error: {exc.detail}")
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

@app.exception_handler(RequestValidationError)
async def validation_error_handler(request, exc):
    logger.warning(f"Validation error: {exc.errors()}")
    return JSONResponse(status_code=400, content={"detail": exc.errors()})

@app.exception_handler(Exception)
async def general_error_handler(request, exc):
    logger.critical(f"Unhandled exception: {exc}")
    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/ping", tags=["Health"])
def ping(db=Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "healthy", "db": "connected", "version": "1.0.0"}
    except Exception:
        return JSONResponse(status_code=500, content={"status": "unhealthy", "db": "error"})


@app.get("/auth", tags=["Auth"])
def get_auth_token():
    return {"Authorization": "Bearer " + os.getenv("SECRET_TOKEN")}


app.include_router(predict.router, prefix="/api/v1/predict", tags=["Prediction"])
app.include_router(weather.router, prefix="/api/v1/weather", tags=["Weather"])
app.include_router(wialon.router, prefix="/api/v1/wialon", tags=["Wialon"])


@app.get("/", tags=["Root"])
def read_root():
    return {
        "project": "Logistic.ai",
        "docs": "/docs",
        "health": "/ping",
        "api": ["/api/v1/predict", "/api/v1/weather", "/api/v1/wialon"],
        "version": "1.0.0"
    }