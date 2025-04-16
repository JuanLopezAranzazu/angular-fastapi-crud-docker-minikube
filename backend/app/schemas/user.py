from pydantic import BaseModel
from typing import Optional

# Esquema base para el usuario
class UserBase(BaseModel):
  username: str
  email: str
  full_name: Optional[str] = None

# Esquema para crear un nuevo usuario
class UserCreate(UserBase):
  password: str  # no hashed aún

# Esquema para actualizar un usuario existente
class UserUpdate(BaseModel):
  username: Optional[str] = None
  email: Optional[str] = None
  full_name: Optional[str] = None
  password: Optional[str] = None

# Esquema para la respuesta del usuario
class UserResponse(UserBase):
  id: int

  class Config:
    from_attributes = True

