
from flask import render_template,request,redirect,url_for
from app import app
from .request import get_news,search_new, get_sources
from .Models import reviews
from .forms import ReviewForm
Review = reviews.Review
@app.route('/')
def index():
        '''
        View movie page function that returns the movie details page and its data
        '''
        popular_news = get_sources('popular')
        title = 'Home - Welcome to The best news  Review Website Online'
        return render_template('index.html', title = title,popular = popular_news)

@app.route('/search/<new_name>')
def search(new_name):
        new_name_list = new_name.split(" ")
        new_name_format = "+".join(new_name_list)
        searched_news = search_new(new_name_format)
        title = f'search articles" for {new_name}'
        return render_template('search.html',news = searched_news)

@app.route('/new/<id>')
def new_review(id):
        news= get_news(id)

        title = 'Article'
        return render_template('news.html',title = title, news=news)