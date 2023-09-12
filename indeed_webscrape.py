# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 11:57:46 2023

@author: Joel Leaman
"""

from bs4 import BeautifulSoup as bs
import json
import pandas as pd
import requests
import httpx

from urllib.request import Request, urlopen

browser_headers_file = 'browser_headers.json'


test_search_term = 'data analyst'


def get_search_results(search_term):
    search_term = search_term.replace(' ', '+')
    url = 'https://uk.indeed.com/jobs?q=' + search_term
    html = requests.get(url).text
    #html = urlopen(req)
    bs_object = bs(html, 'html.parser')
    return bs_object


def test_scrape(search_term):
    
    header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Connection": "keep-alive",
    "Accept-Language": "en-GB,en;q=0.9"
    }
    
    search_term = search_term.replace(' ', '+')
    url = 'https://uk.indeed.com/jobs?q=' + search_term
    
    response = httpx.get(url, headers = header)
    print(response)
    
    return


def test_httpx_scrape(search_term):    
    import httpx

    # Define the headers, including the User-Agent
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
    
    # URL for the initial request
    initial_url = 'https://uk.indeed.com/'
    
    # Make the initial request and get cookies
    with httpx.Client() as client:
        response_initial = client.get(initial_url, headers=headers)
        cookies_from_initial = response_initial.cookies
    
        # Print the cookies (for demonstration purposes)
        print('Initial cookies')
        print('#' * 10)
        print(cookies_from_initial)
        
        print()
        # Make a subsequent request with the captured cookies
        search_term = test_search_term.replace(' ', '+')
        url = 'https://uk.indeed.com/jobs?q=' + test_search_term
        response_subsequent = client.get(url, headers=headers)
    
        # Print the subsequent response (for demonstration purposes)
        print('Response')
        print('#' * 10)
        print(cookies_from_initial)
        print(response_subsequent.text)

test_httpx_scrape(test_search_term)