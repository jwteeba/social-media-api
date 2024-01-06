from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    drivername: str
    dbusername: str
    password: str
    host: str
    database: str

    model_config = SettingsConfigDict(env_file=".env")
