from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from quarkboard.models.base import BaseModel


engine = create_engine(
    "sqlite:///quarkboard.db:",
    echo=True
)
BaseModel.metadata.create_all(engine)

session = Session(engine)
session.close()