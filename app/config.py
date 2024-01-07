from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    drivername: str
    dbusername: str
    password: str
    host: str
    database: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    model_config = SettingsConfigDict(env_file=".env")
