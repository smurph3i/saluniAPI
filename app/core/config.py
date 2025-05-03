from pydantic_settings import BaseSettings, SettingsConfigDict  # New in v2


class Settings(BaseSettings):
    PROJECT_NAME: str = "SaluniAPI"
    DEBUG: bool = True
    API_V1_PREFIX: str = "/api/v1"

    POSTGRES_USER: str = "random_user"  # Placeholder
    POSTGRES_PASSWORD: str = "random_password"  # Placeholder
    POSTGRES_DB: str = "saluniAPI"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str = 5433

    # Read configuration from .env file (model_config in Pydantic v2)
    model_config = SettingsConfigDict(
        env_file=".env",  # Load environment variables from .env
        case_sensitive=True
    )

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


# Instantiate settings object to use the loaded configuration
settings = Settings()
print(settings.project_name)  # Should print "SaluniAPI"
# Should print the full DB URI using .env values
print(settings.sqlalchemy_database_uri)
