import os
from pydantic_settings import BaseSettings
from pydantic import Field
from app import models  # This registers the models with SQLAlchemy's Base


class Settings(BaseSettings):
    project_name: str = Field(default="SaluniAPI", alias="PROJECT_NAME")
    api_version: str = Field(default="v1", alias="API_VERSION")

    database_url: str = Field(alias="DATABASE_URL")
    test_database_url: str = Field(alias="TEST_DATABASE_URL")

    secret_key: str = Field(alias="SECRET_KEY")
    algorithm: str = Field(default="HS256", alias="ALGORITHM")
    access_token_expire_minutes: int = Field(
        default=30, alias="ACCESS_TOKEN_EXPIRE_MINUTES")

    @property
    def actual_database_url(self) -> str:
        """Switches between dev and test DB based on the TESTING flag."""
        if os.getenv("TESTING") == "1":
            return self.test_database_url
        return self.database_url

    model_config = {
        "populate_by_name": True,
        "env_file": ".env",
        "extra": "ignore",
    }


settings = Settings()
