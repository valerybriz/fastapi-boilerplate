from fastapi import APIRouter

from .endpoints.authentication import router as auth_router
from .endpoints.user import router as user_router


router = APIRouter()
router.include_router(auth_router)
router.include_router(user_router)
