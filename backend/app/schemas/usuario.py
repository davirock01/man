from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# Base schemas
class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr
    rol: str  # CONDUCTOR, COORDINADOR, TECNICO, ADMIN
    telefono: Optional[str] = None


class UsuarioCreate(UsuarioBase):
    password: str


class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[EmailStr] = None
    telefono: Optional[str] = None
    estado: Optional[str] = None
    notas: Optional[str] = None


class UsuarioResponse(UsuarioBase):
    id: int
    estado: str
    mfa_enabled: bool
    creado_en: datetime
    ultimo_acceso: Optional[datetime] = None
    
    class Config:
        from_attributes = True


# Auth schemas
class LoginRequest(BaseModel):
    email: EmailStr
    password: str
    mfa_token: Optional[str] = None


class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    usuario: UsuarioResponse


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class RefreshTokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class MFASetupRequest(BaseModel):
    usuario_id: int


class MFASetupResponse(BaseModel):
    secret: str
    qr_uri: str
    backup_codes: list[str]


class MFAVerifyRequest(BaseModel):
    usuario_id: int
    token: str


class MFAVerifyResponse(BaseModel):
    verified: bool
    message: str


