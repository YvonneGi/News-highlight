from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news,get_new,search_article
from .forms import ReviewForm
from ..models import Review

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    popular_news = get_news('popular')
    title = 'Home - Welcome to The best News Review Website Online'
    
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
  news= get_news(id)
  return render_template('news.html',title = title, news=news)

  