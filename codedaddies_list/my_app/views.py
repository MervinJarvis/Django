from django.shortcuts import render
from requests import models
from requests.compat import quote_plus
from bs4 import BeautifulSoup
from . import models
import requests

# Create your views here.
BASE_CRAGLIST_URL='https://losangeles.craigslist.org/search/?query={}'
BASE_CRAGLIST_IMAGE="https://images.craigslist.org/{}_300x300.jpg"

def home(request):
    return render(request,"base.html")

def new_search(request):
    search=request.POST.get('search')
    models.Search.objects.create(search=search)
    final_url=BASE_CRAGLIST_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data=response.text
    soup=BeautifulSoup(data,features="html.parser")
    post_listings=soup.find_all('li',{'class':'result-row'})
    #print(post_listings)
    final_postings=[]

    for post in post_listings:
        post_title=post.find(class_='result-title').text
        post_url=post.find('a').get('href')

        if post.find(class_='result-price'):
            post_price=post.find(class_='result-price').text
        else:
            post_price='N/A'

        if post.find(class_='result-image').get('data-ids'):
            post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
            print(post_image_id)
            post_image_id=BASE_CRAGLIST_IMAGE.format(post_image_id)
        else:
            post_image_id = 'https://craigslist.org/images/peace.jpg'

        final_postings.append((post_title,post_url,post_price, post_image_id))

    #print(data)
    stuff_for_frontend={
        'search':search,
        'final_postings':final_postings,
    }
    return render(request,"my_app/new_search.html",context=stuff_for_frontend)