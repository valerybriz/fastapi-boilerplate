from motor.motor_asyncio import AsyncIOMotorClient

from ..core.config import MAX_CONNECTIONS_COUNT
from ..core.config import MIN_CONNECTIONS_COUNT
from ..core.config import MONGODB_URI
from ..core.config import logger
from ..crud.user import create_user
from ..models.user import UserInCreate
from .mongodb import db


async def connect_to_mongo():
    logger.info("connecting to mongo")
    if MONGODB_URI:
        db.client = AsyncIOMotorClient(
            str(MONGODB_URI),
            maxPoolSize=MAX_CONNECTIONS_COUNT,
            minPoolSize=MIN_CONNECTIONS_COUNT,
        )
        data = {"email": "0@gmail.com", "password": "0", "username": "0"}
        # try to create a sample user
        # raise exception if something fails
        await create_user(db.client, UserInCreate(**data))

        logger.info("connected！")
    else:
        logger.info("MONGODB_URL not found")


async def close_mongo_connection():
    logger.info("closing the connection...")
    if MONGODB_URI:
        db.client.close()
        logger.info("connection closed！")
    else:
        logger.info("nothing closed")
