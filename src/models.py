from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Numeric, Integer

Base = declarative_base()


class InitialStats(Base):
    __tablename__ = "Initial Stats"
    primary_key = Column(String, primary_key=True)
    weight_metric = Column(Numeric, nullable=False)
    weight_imperial = Column(Numeric, nullable=False)
    height_metric = Column(Numeric, nullable=False)
    height_imperial = Column(Numeric, nullable=False)
    gender = Column(String)
    age = Column(Integer)


class TargetStats(Base):
    __tablename__ = "Target Stats"
    primary_key = Column(String, primary_key=True)
    weight_metric = Column(Numeric, nullable=False)
    weight_imperial = Column(Numeric, nullable=False)

