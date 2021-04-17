from fastapi import APIRouter
from fastapi import Depends
from starlette.exceptions import HTTPException
from starlette.status import HTTP_200_OK
from starlette.status import HTTP_400_BAD_REQUEST

from ....core.jwt import get_current_user_authorizer
from ....models.data import Item
from ....models.data import ItemInParse
from ....models.user import User
from ....core.config import logger
router = APIRouter()


@router.get(
    "/hello_world",
    tags=["data"],
    status_code=HTTP_200_OK,
    response_model=Item,
)
async def get_argo_workflow_status(
    content: ItemInParse,
    user: User = Depends(get_current_user_authorizer()),
):
    if not content.message:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=f"Couldn't find the client_id: {content}",
        )

    logger.info(f"message: {content.message}")
    item = Item()
    item.message = content.message
    return item
