from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    ACCESS_KEY: str
    SECRET_KEY: str
    ENDPOINT_URL: str
    BUCKET_NAME: str
    REGION: str

    model_config = SettingsConfigDict(env_file=".env")


CONFIG = Config()
