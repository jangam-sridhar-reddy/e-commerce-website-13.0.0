from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, DateTime
from datetime import datetime, timezone

from app.database.database import session

Base = declarative_base()

Base.query = session.query_property()

class TimeStampedModel(Base):
    __abstract__ = True
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=None, onupdate=datetime.now(timezone.utc))
    