from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from app.config.openapi import tags_metadata
from app.middlewares.errorHandler import (
  http_error_handler,
  sqlalchemy_error_handler,
  general_error_handler
)
from app.routes import user
from app.config.database import Base, engine

app = FastAPI(
  openapi_tags=tags_metadata,
)

origins = [
  "http://localhost:4200"
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.get("/")
async def root():
  return {"message": "Welcome to the FastAPI application!"}

# Agregar los routers de las aplicaciones
app.include_router(user.router, tags=["user"], prefix="/api/v1/user")

# Agregar los middlewares de error
app.add_exception_handler(HTTPException, http_error_handler)
app.add_exception_handler(SQLAlchemyError, sqlalchemy_error_handler)
app.add_exception_handler(Exception, general_error_handler)

# Crear las tablas en la base de datos
@app.on_event("startup")
def startup_event():
  try:
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
