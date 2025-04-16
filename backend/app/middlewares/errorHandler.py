from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

# Middleware para manejar errores HTTP
async def http_error_handler(request: Request, exc: HTTPException):
  return JSONResponse(
    status_code=exc.status_code,
    content={"detail": exc.detail},
  )

# Middleware para manejar errores de SQLAlchemy
async def sqlalchemy_error_handler(request: Request, exc: SQLAlchemyError):
  return JSONResponse(
    status_code=500,
    content={"detail": "A database error occurred."},
  )

# Middleware para manejar errores generales
async def general_error_handler(request: Request, exc: Exception):
  return JSONResponse(
    status_code=500,
    content={"detail": "An internal server error occurred."},
  )
