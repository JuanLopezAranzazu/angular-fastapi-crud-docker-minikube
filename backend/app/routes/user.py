from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.config.database import get_db
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet

# Generar una clave de cifrado
key = Fernet.generate_key()
cipher_suite = Fernet(key)

router = APIRouter()

# Endpoint para obtener todos los usuarios con paginación
# Ejemplo de uso: /api/v1/user/paginated?skip=0&limit=10
@router.get("/paginated", response_model=List[UserResponse])
def get_paginated_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
  users = db.query(User).offset(skip).limit(limit).all()
  if not users:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="No users found"
    )
  return users

# Endpoint para obtener todos los usuarios
@router.get("/", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
  users = db.query(User).all()
  if not users:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="No users found"
    )
  return users

# Endpoint para obtener un usuario por ID
@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
  user = db.query(User).filter(User.id == user_id).first()
  if not user:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="User not found"
    )
  return user

# Endpoint para crear un nuevo usuario
@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
  db_user = db.query(User).filter(User.email == user.email).first()
  if db_user:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="Email already registered"
    )
  new_user = User()
  new_user.full_name = user.full_name
  new_user.username = user.username
  new_user.email = user.email
  new_user.hashed_password = cipher_suite.encrypt(user.password.encode()).decode()

  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user

# Endpoint para actualizar un usuario
@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
  db_user = db.query(User).filter(User.id == user_id).first()
  if not db_user:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="User not found"
    )
  
  if user.email:
    email_exists = db.query(User).filter(User.email == user.email).first()
    if email_exists and email_exists.id != user_id:
      raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Email already registered"
      )
    db_user.email = user.email

  if user.full_name:
    db_user.full_name = user.full_name
  
  if user.username:
    db_user.username = user.username

  if user.password:
    db_user.hashed_password = cipher_suite.encrypt(user.password.encode()).decode()

  db.commit()
  db.refresh(db_user)
  return db_user

# Endpoint para eliminar un usuario
@router.delete("/{user_id}", response_model=UserResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
  db_user = db.query(User).filter(User.id == user_id).first()
  if not db_user:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="User not found"
    )
  db.delete(db_user)
  db.commit()
  return db_user