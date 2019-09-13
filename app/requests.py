import urllib.request,json
from .models import News_source
form .models import News_article

# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url,base_source_url
    api_key = app.config['News_API_KEY']
    base_url = app.config['News_API_BASE_URL']
    base_sources_url = app.config['NEWS_SOURCES_BASE_URL']
    
