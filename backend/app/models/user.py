from sqlalchemy import Column, Integer, String
from app.config.database import Base

# Modelo de usuario para la base de datos
class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True, index=True)
  username = Column(String, unique=True, index=True, nullable=False)
  email = Column(String, unique=True, index=True, nullable=False)
  hashed_password = Column(String, nullable=False)
  full_name = Column(String, nullable=True)
