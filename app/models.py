class News_source:
    '''
    News_source class to define News_source Objects
    '''

    def __init__(self,id,name,description,url,country,language,category):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.language = language
        self.country = country
        self.category = category
class News_article:
    '''
    News_article class to define News_article Objects
    '''

    def __init__(self,title,author,description,url,urlImage,publishedAt,content):
        self.title =title
        self.author = author
        self.description = description
        self.url = url
        self.urlImage = urlImage
        self.publisheAt = publisheAt
        self.content = content



class Review:

    all_reviews = []

    def __init__(self,news_id,title,name,author,description,url, urlToImage,publishedAt,content):
        self.new_id = new_id
        self.title = title
        self.name= name
        self.author=author
        self.description=description
        self.url=link
        self.urlToImage= imageurl
        self.publishedAt = date
        self.content=content
       

    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()