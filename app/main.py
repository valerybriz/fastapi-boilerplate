from fastapi import FastAPI
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

from .api.api_v1.api import router as api_router
from .core.config import ALLOWED_HOSTS
from .core.config import API_V1_STR
from .core.config import PROJECT_NAME
from .core.errors import http_422_error_handler
from .core.errors import http_error_handler
from .db.mongodb_utils import close_mongo_connection
from .db.mongodb_utils import connect_to_mongo

app = FastAPI(title=PROJECT_NAME)

if not ALLOWED_HOSTS:
    ALLOWED_HOSTS = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

app.add_exception_handler(HTTPException, http_error_handler)
app.add_exception_handler(
    HTTP_500_INTERNAL_SERVER_ERROR, http_422_error_handler
)

app.include_router(api_router, prefix=API_V1_STR)
