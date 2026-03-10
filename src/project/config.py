## @file config.py
#  @author Sean Duffie
#  @brief This file allows us to automatically pull secret envrionment variables from a local .env file

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """!
    @brief This will automatically look for an 'API_KEY' environment variable or .env entry
    @param BaseSettings Parent Class that is inherited
    @exception ValueError The API KEY was not found in the .env file.
    """

    api_key: str = "123"
    database_url: str = "sqlite:///./test.db"  # Default value if not provided

    model_config = SettingsConfigDict(env_file=".env")


## @var settings
#  Create a singleton instance of the environment variables to be used elsewhere
settings = Settings()
