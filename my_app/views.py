from django.shortcuts import render
from requests.compat import quote_plus
import requests
from bs4 import BeautifulSoup
from . import models

# Create your views here.

BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/?query={}'

def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')

    post_listings = soup.find_all('li', {'class': 'result-row'})
    post_title = post_listings[0].find(class_='result-title').text
    post_url = post.find()

    print(posts_titiles[0].get('href'))
    stuff_for_frontend = {
        'search': search,
    }
    return render(request, 'my_app/new_search.html', stuff_for_frontend)