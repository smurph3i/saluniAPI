from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    project_name: str = Field(default="SaluniAPI", alias="PROJECT_NAME")
    api_version: str = Field(default="v1", alias="API_VERSION")

    database_url: str = Field(alias="DATABASE_URL")

    secret_key: str = Field(alias="SECRET_KEY")
    algorithm: str = Field(default="HS256", alias="ALGORITHM")
    access_token_expire_minutes: int = Field(
        default=30, alias="ACCESS_TOKEN_EXPIRE_MINUTES")

    model_config = {
        "populate_by_name": True,
        "env_file": ".env",
        "extra": "ignore",
    }


settings = Settings()
