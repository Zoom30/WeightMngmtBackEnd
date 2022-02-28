from typing import Optional

from pydantic import BaseSettings


class CommonSettings(BaseSettings):
    db_host: Optional[str]
    db_user: Optional[str]
    db_pass: Optional[str]
    db_name: Optional[str]
    db_port: Optional[int]


settings = CommonSettings()
