from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time
def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)
def scrape():
    browser = init_browser()
    mars = {}
    # Retrieve Latest News Article
    url = 'http://breachlevelindex.com/data-breach-database'
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')
