from fastapi import APIRouter

router = APIRouter(prefix="/api")

# Import your API routes here
from . import users

router.include_router(users.router, prefix="/users", tags=["users"])
