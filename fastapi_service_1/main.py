from fastapi import FastAPI
import logging
from logging.handlers import RotatingFileHandler

app = FastAPI()

log_handler = RotatingFileHandler(
    "/var/log/fastapi/app.log", maxBytes=2000000, backupCount=10
)
log_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
log_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

@app.get("/")
def read_root():
    logger.info("Root endpoint was accessed.")
    return {"message": "Hello from FastAPI"}

@app.get("/health")
def health_check():
    logger.info("Health check endpoint was accessed.")
    return {"status": "healthy"}
