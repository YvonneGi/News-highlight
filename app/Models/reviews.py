class Review:

    all_reviews = []

    def __init__(self,news_id,title,name,author,description,url, urlToImage,publishedAt,content):
        self.new_id = new_id
        self.title = title
        self.name= name
        self.author=author
        self.description=description
        self.url=link
        self.  urlToImage= imageurl
        self.publishedAt = date
        self.content=content
       

    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()
