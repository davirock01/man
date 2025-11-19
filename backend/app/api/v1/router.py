from fastapi import APIRouter

from app.api.v1 import auth, conductor, coordinador, tecnico, admin

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(conductor.router, prefix="/conductor", tags=["conductor"])
api_router.include_router(coordinador.router, prefix="/coordinador", tags=["coordinador"])
api_router.include_router(tecnico.router, prefix="/tecnico", tags=["tecnico"])
api_router.include_router(admin.router, prefix="/admin", tags=["admin"])


