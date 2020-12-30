#!/usr/bin/env python
# coding: utf-8

#Dependencies
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import requests
import os
import json
import time
import pandas as pd


# In[2]:

def init_chrome():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser

# In[3]:

def mars_news():
    browser = init_chrome()
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    return_list = []
    # In[4]:
    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(html, 'html.parser')
    #print(soup.prettify())

    content = soup.find("div", class_ ='content_page')

    # In[6]:
    #Extract title text
    news_title = content.find_all("div", class_ ='content_title')

    n0 =news_title[0].text.strip()


    # In[7]:


    # Print all latest paragraph texts
    paragraphs = content.find_all("div", class_ = 'article_teaser_body')
    p0 =paragraphs[0].text
    browser.quit()
    return_list.append ({'newsTitle':n0,'newsText':p0})
    return (return_list)
    

# # JPL Mars Space Images - Featured Image 

# In[8]:

def JPL_image():
    browser = init_chrome()
    url ='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    browser.find_by_id("full_image").click()
    browser.find_by_text("more info     ").click()
    html = browser.html
    soup = bs(html, 'html.parser')
    featured_img = soup.find("img", class_='main_image')['src']
    pic_url = f"https://www.jpl.nasa.gov{featured_img}"
    browser.quit()
    return pic_url
    


# # Mars Facts

def Mars_Facts():
    browser =init_chrome()
    returned_facts_list = []
    Mars_facts_url = 'https://space-facts.com/mars/'
    browser.visit(Mars_facts_url)
    Mars_facts = pd.read_html(Mars_facts_url)
    Mars_facts
    rights = list(Mars_facts[0][0])
    lefts = list(Mars_facts[0][1])
    for i in range (len (rights)):
        returned_facts_list.append ({rights[i].strip(":"): lefts [i]})
    browser.quit()    
    return returned_facts_list
    
    
    

 # Mars Hemispheres

def Mars_Hemispheres():
    browser =init_chrome ()

    USGS_Astrogeology_url =  'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    base_USGS_URL = USGS_Astrogeology_url.split('gov/')[0]
    browser.visit(USGS_Astrogeology_url)
    print (USGS_Astrogeology_url)
    html = browser.html
    soup =bs(html, 'html.parser')
    visit_list = []
    clicks = soup.find_all('a', class_='itemLink product-item')

    for items in clicks:
        temps_st = base_USGS_URL+ str(items).split('href=')[1].split('>')[0].strip ('"')
        temps_st = temps_st.replace("//","/")
        if temps_st not in visit_list:
            visit_list.append (temps_st)
    print (visit_list)

    img_url_list = []
    title_list = []
    i = 0
    for i in range (len (visit_list)):
        browser.visit(visit_list [i])
        html = browser.html
        soup = bs(html, 'html.parser')
        title = soup.find_all('h2', class_='title')
        img_url = soup.find_all('a')[4]
        title_list.append (str(title).split('>')[1].split('<')[0])
        img_url_list.append (str(img_url).split('"')[1])

    print (title_list)
    print (img_url_list)

    hemisphere_image_urls = []
    for i in range (len (img_url_list)):
        hemisphere_image_urls.append ({'title': title_list[i], 'img_url': img_url_list [i]})
        print (hemisphere_image_urls[i]['title'])
        print (hemisphere_image_urls[i]['img_url'] + '\n')
    print (hemisphere_image_urls)
    browser.quit()
    return hemisphere_image_urls