from pydantic_settings import BaseSettings


class BaseSettingsWithEnv(BaseSettings):
    # 配置读取方式
    model_config = {"env_file": ".env", "extra": "ignore"}  # env文件的位置


# 通用配置
class CommonSettings(BaseSettingsWithEnv):
    environment: str = "development"


# web服务配置
class WebSettings(BaseSettingsWithEnv):
    app_name: str = "Web Service API"  # 实际读取 WEB_APP_NAME
    cors_origins: str = ""
    cors_expose_headers: str = ""

    # 配置读取方式
    model_config = {"env_prefix": "WEB_"}


# 数据库配置
class DBSettings(BaseSettingsWithEnv):
    host: str = ""
    port: str = ""
    name: str = ""
    user: str = ""
    password: str = ""

    model_config = {"env_prefix": "DB_"}


common_settings = CommonSettings()
web_settings = WebSettings()
db_settings = DBSettings()
