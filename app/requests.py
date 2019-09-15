import urllib.request,json
from .models import News_source
from .models import News_article
from app import main
News_source = news.News_source
# News_ = News.News
# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url,base_source_url
    api_key = app.config['News_API_KEY']
    base_url = app.config['News_API_BASE_URL']
    base_sources_url = app.config['NEWS_SOURCES_BASE_URL']
def get_news(category):
        '''
        Function that gets the json response to our url request
        '''
        get_news_url ='https://newsapi.org/v2/sources?category&apiKey=f0e6315e7a764546ab83a985c53b139e'


        with urllib.request.urlopen(get_news_url) as url:
                get_news_data = url.read()
                get_news_response = json.loads(get_news_data)
                news_results = None

                if get_news_response['news']:
                        news_results_list = get_news_response['news']
                        news_results = process_results(news_results_list)
        return news_results
def process_results(news_list):
   '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain movie details

    Returns :
        new_results: A list of news objects
    '''
       news_results= []

    for news_item in news_list:
                   
        id = news_item.get('id')   
        name =news_item.get('name')
        description=news_item.get('description')
        url=news_item.get('url')
        country=news_item.get('country')
        language=news_item.get('language')
        category=news_item.get('"category')

        if name:
            news_object = News_source(id,name,description,url, country,language,category)
            news_results.append(news_object)

    return news_results
def get_new(id):
    get_new_details_url = News_base_url.format(id,api_key)

    with urllib.request.urlopen(get_new_details_url) as url:
        new_details_data = url.read()
        new_details_response = json.loads(new_details_data)
        print(new_details_response)
        new_object = None
        art_news=[]
        if new_details_response['articles']:
                for news_item in new_details_response['articles']:
                        title = news_item.get('title')
                        author=news_item.get('author')
                        description=news_item.get('description')
                        url=news_item.get('url')
                        urlToImage=news_item.get('urlToImage')
                        publishedAt =news_item.get('publishedAt')
                        content = news_item.get('content')
                        new_object = News(title,author,description,url,urlToImage,publishedAt,content)
                        art_news.append(new_object)

        return art_news
def search_new(new_name):
    search_new_url = 'https://newsapi.org/v2/everything?q=bitcoin&from=2019-09-13&sortBy=publishedAt&apiKey=f0e6315e7a764546ab83a985c53b139e?api_key={}&query={}'.format(api_key,new_id)
    with urllib.request.urlopen(search_new_url) as url:
        search_new_data = url.read()
        search_new_response = json.loads(search_new_data)
        search_new_articles = None

    if search_new_response['articles']:
        search_new_list = search_new_response['articles']
        search_new_articles = process_articles(search_new_list)


        return search_new_articles


        


    
