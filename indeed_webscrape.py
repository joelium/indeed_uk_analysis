# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 11:57:46 2023

@author: Joel Leaman
"""

from bs4 import BeautifulSoup as bs
import json
import pandas as pd
import requests

from urllib.request import Request, urlopen

def get_search_results(search_term):
    search_term = search_term.replace(' ', '+')
    url = 'https://uk.indeed.com/jobs?q=' + search_term
    html = requests.get(url).text
    #html = urlopen(req)
    bs_object = bs(html, 'html.parser')
    return bs_object

print(get_search_results('data analyst'))