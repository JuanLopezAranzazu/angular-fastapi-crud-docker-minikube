from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException
from sqlalchemy.exc import SQLAlchemyError, OperationalError
from app.config.openapi import tags_metadata
from app.middlewares.errorHandler import (
  http_error_handler,
  sqlalchemy_error_handler,
  general_error_handler
)
from app.routes import user
from app.config.database import Base, engine
import time

app = FastAPI(
  openapi_tags=tags_metadata,
)

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
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

def wait_for_db(engine, retries=10, delay=2):
  for i in range(retries):
    try:
      conn = engine.connect()
      conn.close()
      print("Database connection successful.")
      return
    except OperationalError:
      print(f"Retrying to connect to the database in {delay} seconds... ({i + 1}/{retries})")
      time.sleep(delay)
  raise Exception("Could not connect to the database after several retries.")


# Crear las tablas en la base de datos
@app.on_event("startup")
def startup_event():
  try:
    wait_for_db(engine)
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")
  except Exception as e:
    print(f"Error creating database tables: {e}")
    raise HTTPException(status_code=500, detail=str(e))
