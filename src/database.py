"""
Module described database connection in application.
Module used SQLAlchemy Core to build SQL Queries and define tables realtions.
"""
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from src import config
from src import models

engine = sa.create_engine(config.DATABASE_URL, connect_args={"check_same_thread": False})
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    models.Base.metadata.create_all(bind=engine)
