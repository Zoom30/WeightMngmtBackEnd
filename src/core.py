from sqlalchemy.orm import sessionmaker, scoped_session

from src.database_engine import engine


class Core:
    def __init__(self):
        core_session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        self.core_session = scoped_session(core_session_factory)
