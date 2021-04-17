import logging
from os import getenv

from starlette.datastructures import CommaSeparatedStrings
from starlette.datastructures import Secret

logger = logging.getLogger("fastapi boilerplate")

API_V1_STR = "/api/v1"
JWT_TOKEN_PREFIX = "Token"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # one week

SECRET_KEY = Secret(getenv("SECRET_KEY", "secret key for project"))
MAX_CONNECTIONS_COUNT = int(getenv("MAX_CONNECTIONS_COUNT", 10))
MIN_CONNECTIONS_COUNT = int(getenv("MIN_CONNECTIONS_COUNT", 10))
PROJECT_NAME = getenv("PROJECT_NAME", "FastAPI example application")
ARGO_API_TIMEOUT = 60
ALLOWED_HOSTS = CommaSeparatedStrings(getenv("ALLOWED_HOSTS", ""))

MONGO_HOST = getenv("MONGO_HOST")
MONGO_PORT = getenv("MONGO_PORT")
MONGO_USER = getenv("MONGO_USER")
MONGO_PASSWORD = getenv("MONGO_PASSWORD")
MONGO_DB = getenv("MONGO_DB")

DATABASE_NAME = getenv("MONGO_DB")
USERS_COLLECTION_NAME = "users"
MONGODB_URI = (
    f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}"
)

RESOURCES_PATH = "app/resources"
