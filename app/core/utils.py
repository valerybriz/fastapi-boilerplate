import ast
import json
from typing import Tuple

import requests
import yaml
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from requests.exceptions import ConnectionError
from starlette.responses import JSONResponse
from .config import logger


def load_json_file(file_path):
    """Obtains the information of a Json dump and stores
    it as an array of json's"""
    new_json_array = []
    error = None
    try:
        with open(file_path, "r") as json_file:
            new_json_array = [
                json.loads(line) for line in json_file.readlines()
            ]
    except Exception as e:
        error = "Error trying to load json file"
        logger.error(f"{error}: {e}")

    return new_json_array, error
