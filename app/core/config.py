from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@db:5432/qa_db"
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
