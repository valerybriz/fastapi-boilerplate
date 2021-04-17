from fastapi import APIRouter
from fastapi import BackgroundTasks
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK
from starlette.status import HTTP_400_BAD_REQUEST
from starlette.status import HTTP_401_UNAUTHORIZED

from ....core.jwt import get_current_user_authorizer
from ....models.data import Item
from ....models.data import ItemInParse
from ....models.user import User
from ....core.config import logger
from ....core.utils import dummy_function
from ....core.utils import dummy_background_task

router = APIRouter()


@router.post(
    "/hello_world",
    tags=["data"],
    status_code=HTTP_200_OK,
    response_model=Item,
)
async def post_message(
    content: ItemInParse,
    # user: User = Depends(get_current_user_authorizer()),
):

    if not content.message:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=f"Couldn't find the message: {content}",
        )

    result = await dummy_function(content.message)
    item = Item()
    item.message = result
    item.status = "OK"
    return item


@router.post(
    "/hello_world_async",
    tags=["data"],
    status_code=HTTP_200_OK,
    response_model=Item,
)
async def post_message_async(
    content: ItemInParse,
    # user: User = Depends(get_current_user_authorizer()),
):

    if not content.message:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=f"Couldn't find the message: {content}",
        )

    backgroundtask = BackgroundTasks()
    backgroundtask.add_task(
        dummy_background_task, content.message
    )

    return JSONResponse(
        {"status": "Starting dummy background task"}, background=backgroundtask,
    )

    #item = Item()
    #item.message = content.message
    #item.status = "OK"
    #return item
