#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pymongo 
from flask import Flask, render_template
import datetime as dt
import time

def scrape():

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

#Mars News

url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
browser.visit(url)

html = browser.html
soup = bs(html,'html.parser')

news = soup.find('div',class_='list_text')

news_title = news.find('div',class_='content_title').get_text()

news_text = news.find('div',class_='article_teaser_body').get_text()
news_text

#JPL Images

url = "https://www.jpl.nasa.gov/images?search=&category=Mars"
browser.visit(url)


browser.find_by_css('.BaseImage').click()


html = browser.html
soup = bs(html,'html.parser')

page = soup.find('img',class_='BaseImage')

page=soup.find(id='SearchListingPageResults')


image=page['data-src']

image

featured_img_url = f'{image}'
featured_img_url

url_2 = "https://space-facts.com/mars/"
table = pd.read_html(url_2)[0]
table

url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)


hemisphere_image_urls = []
hem_links = browser.find_by_css('.description')
len(hem_links)


list(hem_links)

for i in range(len(hem_links)):
    print(hem_links[i].find_by_tag('a').find_by_tag('h3').html, end='\n\n')

for i in range(len(hem_links)):
    hem = {}
    title_list = []
    url_hem = {}
    url_list = []
    hem_links = browser.find_by_css('.description')
    time.sleep(2)
    hem_links[i].find_by_tag('a').find_by_tag('h3').click()
    title_list.append(browser.find_by_tag('section').find_by_css('.title').html)
    image = browser.find_by_tag('li').find_by_tag('a')
    url_list.append(image['href'])
    hem['title'] = title_list
    url_hem['url'] = url_list
    time.sleep(2)
    hem['title'] = title_list
    hem['url'] = url_list
    browser.back()
    print(hem)
    hemisphere_image_urls.append(hem)

print(hemisphere_image_urls)