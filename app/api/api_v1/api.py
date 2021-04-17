from fastapi import APIRouter

from .endpoints.authentication import router as auth_router
from .endpoints.user import router as user_router
from .endpoints.data import router as data_router


router = APIRouter()
router.include_router(auth_router)
router.include_router(user_router)
router.include_router(data_router)
