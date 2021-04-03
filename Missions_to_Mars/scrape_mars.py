#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pymongo 
from flask import Flask, render_template
import datetime as dt
import requests


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


news_title = "NASA Ingenuity Mars Helicopter Prepares for First Flight"
news_p = "Now uncocooned from its protective carbon-fiber shield, the helicopter is being readied for its next steps."


# In[4]:


url = "https://www.jpl.nasa.gov/images?search=&category=Mars"
browser.visit(url)


# In[6]:


html = browser.html
soup = bs(html,'html.parser')


# In[16]:


page=soup.find(id='SearchListingPageResults')


# In[17]:


image=page.find('img')


# In[18]:


image


# In[19]:


image['src']


# In[21]:


featured_img_url = 'https://d2pn8kiwq2w21t.cloudfront.net/images/jpegPIA24510.2e16d0ba.fill-400x400-c50.jpg'


# In[20]:


url_2 = "https://space-facts.com/mars/"
table = pd.read_html(url_2)
table


# In[ ]:


hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
]

