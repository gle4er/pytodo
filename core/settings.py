from functools import lru_cache

from pydantic import (
    BaseSettings,
    PostgresDsn,
)


class Settings(BaseSettings):
    pg_dsn: PostgresDsn = 'postgresql://postgres:postgres@postgres/postgres'

    class Config:
        env_prefix = 'PYTODO_'
        env_file = '.env'
        env_file_encoding = 'utf-8'


@lru_cache
def get_settings():
    return Settings()
