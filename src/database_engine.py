import os

from sqlalchemy import create_engine
from src.settings import settings
db_uri = os.environ.get(
    "DB_URI", f"postgresql://{settings.db_user}:{settings.db_pass}@{settings.db_host}:{settings.db_port}/{settings.db_name}"
)
engine = create_engine(db_uri, echo=True)
