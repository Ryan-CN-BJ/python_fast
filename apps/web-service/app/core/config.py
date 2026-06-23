from pydantic_settings import BaseSettings


class _BseEnvSetting(BaseSettings):
    model_config = {"env_file": ".env", "extra": "ignore"}


class _CommonSettings(_BseEnvSetting):
    enviroment: str = "development"


class _WebSettings(_BseEnvSetting):
    app_name: str = "Web Service API"
    model_config = {"env_prefix": "WEB_"}


class _DBSetting(_BseEnvSetting):
    host: str = ""
    port: str = ""
    name: str = ""
    user: str = ""
    password: str = ""

    model_config = {"env_prefix": "DB_"}


commonSetting = _CommonSettings()
webSetting = _WebSettings()
dbSetting = _DBSetting()
