from bson.objectid import ObjectId
from pydantic import EmailStr

from ..core.config import DATABASE_NAME
from ..core.config import USERS_COLLECTION_NAME
from ..db.mongodb import AsyncIOMotorClient
from ..models.user import UserInCreate
from ..models.user import UserInDB
from ..models.user import UserInUpdate


async def get_user(conn: AsyncIOMotorClient, username: str) -> UserInDB:
    row = await conn[DATABASE_NAME][USERS_COLLECTION_NAME].find_one(
        {"username": username}
    )
    if row:
        return UserInDB(**row)


async def get_user_by_email(
    conn: AsyncIOMotorClient, email: EmailStr
) -> UserInDB:
    row = await conn[DATABASE_NAME][USERS_COLLECTION_NAME].find_one(
        {"email": email}
    )
    if row:
        return UserInDB(**row)


async def create_user(conn: AsyncIOMotorClient, user: UserInCreate) -> UserInDB:
    dbuser = UserInDB(**user.dict())
    dbuser.change_password(user.password)

    row = await conn[DATABASE_NAME][USERS_COLLECTION_NAME].insert_one(
        dbuser.dict()
    )

    dbuser.id = row.inserted_id
    dbuser.created_at = ObjectId(dbuser.id).generation_time
    dbuser.updated_at = ObjectId(dbuser.id).generation_time

    return dbuser


async def update_user(
    conn: AsyncIOMotorClient, username: str, user: UserInUpdate
) -> UserInDB:
    dbuser = await get_user(conn, username)

    dbuser.username = user.username or dbuser.username
    dbuser.email = user.email or dbuser.email
    dbuser.bio = user.bio or dbuser.bio
    if user.password:
        dbuser.change_password(user.password)

    updated_at = await conn[DATABASE_NAME][USERS_COLLECTION_NAME].update_one(
        {"username": dbuser.username}, {"$set": dbuser.dict()}
    )
    dbuser.updated_at = updated_at
    return dbuser
