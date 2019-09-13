import os

class Config:

    News_API_BASE_URL ='https://newsapi.org/v2/everything?sources={}&apiKey={}'
    NEWS_SOURCES_BASE_URL='https://newapi.org/v2/sources?category&apiKey=870c6f91cc3244ac9013dcbecb84e54d'
    News_API_KEY = os.environ.get('f0e6315e7a764546ab83a985c53b139e')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}