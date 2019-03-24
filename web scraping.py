# Python 3.6.4 |Anaconda custom (64-bit)| (default, Mar 12 2018, 20:20:50) 
# Created by dponganti on 3/20/2019
import sys
import os
from urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError
import json

# Complete the function below.
# Base url: https://jsonmock.hackerrank.com/api/movies/search/?Title=

def  getMovieTitles(substr):
    url = "https://jsonmock.hackerrank.com/api/movies/search/?Title="+substr
    response = urlopen(url)
    res_data = json.load(response)
    total_pages = res_data['total_pages']

    titles = []
    page = 1
    while page <= total_pages:
        data = res_data['data']
        for d in data:
            titles.append(d['Title'])

        page = page + 1
        response = urlopen(url+"&page="+str(page))
        res_data = json.load(response)

    titles.sort()
    return titles

_substr = "spiderman"
res = getMovieTitles(_substr)
print('\n'.join(res))