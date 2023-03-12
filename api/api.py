from fastapi import APIRouter

from api.endpoints import action


api_router = APIRouter()
api_router.include_router(action.router, prefix="/action", tags=["Action"])
