import time
from .config import logger


async def dummy_function(message: str) -> str:
    logger.warning("Inside dummy_function")
    time.sleep(5)
    logger.warning("Getting back from dummy_function")
    return f"New: {message}"


def dummy_background_task(message: str) -> str:
    logger.warning("Inside dummy_background_task")
    time.sleep(10)
    logger.warning("Getting back from dummy_background_task")
    return f"New Async: {message}"
