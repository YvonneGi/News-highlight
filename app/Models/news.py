class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,title,author,description,url,urlImage,publishedAt,content):
        # self.id =id
        self.title =  title
        
        self.author = author
        self.description = description
        self.url= url
        self.urlImage =urlImage
        self.publishedAt = publishedAt
        self.content=content