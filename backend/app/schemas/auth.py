"""
Schemas para autenticación
"""
from pydantic import BaseModel


class LoginRequest(BaseModel):
    email: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: dict


class UserResponse(BaseModel):
    id: int
    email: str
    nombre: str
    rol: str
    
    class Config:
        from_attributes = True

