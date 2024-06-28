from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str
    db_port: int
    db_password: str
    db_name: str
    db_username: str
    token_secret_key: str
    token_algorithm: str
    token_access_expire_minutes: int

    class Config:
        env_file = ".env"


settings = Settings()
