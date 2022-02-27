from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Numeric

base = declarative_base()

class InitialStats(base):
    __tablename__ = "Initial Stats"
    primary_key = Column(String, primary_key=True)
    weight = Column(Numeric, nullable=False)