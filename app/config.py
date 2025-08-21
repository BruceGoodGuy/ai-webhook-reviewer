from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    GITHUB_API: str = "default_api"
    GITHUB_WEBHOOK_SECRET: str = "default_secret"
    OPEN_AI_API_KEY: str = "default_openai_key"
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
