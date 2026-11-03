from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str
    secret_key: str
    redis_url: str = "redis://localhost:6379"
    db_ssl: bool = True  # False para Postgres local nos testes


settings = Settings()