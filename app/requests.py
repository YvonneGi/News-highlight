import urllib.request,json
from .Models import news
from app import app
from app.Models.source import source

News=news.News
# source = news.source

api_key = app.config['NEWS_API_KEY']
source_base_url= app.config["NEWS_SOURCES_BASE_URL"]
News_base_url = app.config["NEWS_API_BASE_URL"]

def get_sources(category):
        '''
        Function that gets the json response to our url request
        '''
        get_sources_url ='https://newsapi.org/v2/sources?category&apiKey=f0e6315e7a764546ab83a985c53b139e'


        with urllib.request.urlopen(get_sources_url) as url:
                get_sources_data = url.read()
                get_sources_response = json.loads(get_sources_data)
                news_articles = None

                if get_sources_response['sources']:
                        sources_articles_list = get_sources_response['sources']
                        sources_articles = process_articles(sources_articles_list)
        # print(sources_articles)
        return sources_articles

def process_articles(sources_list):
#     print(sources_list)
    source_articles= []
    for news_item in sources_list:
                   
        id = news_item.get('id')   
        name =news_item.get('name')
        description=news_item.get('description')
        url=news_item.get('url')
        country=news_item.get('country')
        language=news_item.get('language')
        category=news_item.get('"category')

        if name:
            news_object = source(id,name,description,url, country,language,category)
            source_articles.append(news_object)

    return source_articles

def get_news(id):
    get_new_details_url = News_base_url.format(id,api_key)

    with urllib.request.urlopen(get_new_details_url) as url:
        new_details_data = url.read()
        new_details_response = json.loads(new_details_data)
        print(new_details_response)
        new_object = None
        abc=[]
        if new_details_response['articles']:
                for news_item in new_details_response['articles']:
                        # id = news_item.get('id')
                        title = news_item.get('title')
                        # name = news_item.get('name')
                        author=news_item.get('author')
                        description=news_item.get('description')
                        url=news_item.get('url')
                        urlToImage=news_item.get('urlToImage')
                        publishedAt =news_item.get('publishedAt')
                        content = news_item.get('content')
                        new_object = News(title,author,description,url,urlToImage,publishedAt,content)
                        abc.append(new_object)

        return abc
def search_new(new_name):
    search_new_url = 'https://newsapi.org/v2/everything?q=bitcoin&from=2019-01-18&sortBy=publishedAt&apiKey=f0e6315e7a764546ab83a985c53b139e?api_key={}&query={}'.format(api_key,new_id)
    with urllib.request.urlopen(search_new_url) as url:
        search_new_data = url.read()
        search_new_response = json.loads(search_new_data)
        search_new_articles = None

    if search_new_response['articles']:
        search_new_list = search_new_response['articles']
        search_new_articles = process_articles(search_new_list)


        return search_new_articles
        


    
