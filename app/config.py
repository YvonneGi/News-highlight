class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='https://newsapi.org/v2/everything?sources={}&apiKey={}'
    NEWS_SOURCES_BASE_URL='https://newapi.org/v2/sources?category&apiKey=f0e6315e7a764546ab83a985c53b139e'
    NEWS_API_KEY ='f0e6315e7a764546ab83a985c53b139e'
    pass



class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True