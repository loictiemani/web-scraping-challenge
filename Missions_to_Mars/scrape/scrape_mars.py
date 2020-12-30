#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Dependencies
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import requests
import os
import json
import time


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

    # In[4]:
    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(html, 'html.parser')
    print(soup.prettify())

    # In[5]:
    content = soup.find("div", class_ ='content_page')

    # In[6]:
    #Extract title text
    news_title = content.find_all("div", class_ ='content_title')

    print(news_title[0].text.strip())


    # In[7]:


    # Print all latest paragraph texts
    paragraphs = content.find_all("div", class_ = 'article_teaser_body')
    paragraphs[0].text

    return (title, paragraph)


# # JPL Mars Space Images - Featured Image
# 

# In[8]:

def JPL_image():
    
url ='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
html = browser.html


# In[9]:


browser.find_by_id("full_image").click()


# In[10]:


browser.find_by_text("more info     ").click()


# In[11]:


html = browser.html
soup = bs(html, 'html.parser')
featured_img = soup.find("img", class_='main_image')['src']


# In[12]:


featured_img


# In[13]:


pic_url = f"https://www.jpl.nasa.gov{featured_img}"
pic_url


# # Mars Facts

# In[14]:


Mars_facts_url = 'https://space-facts.com/mars/'
browser.visit(Mars_facts_url)


# In[15]:


html = browser.html
soup = bs(html, 'html.parser')


# In[16]:


#Mars_fact = soup.find("table", class_ = 'tablepress tablepress-id-p-mars')

#print(Mars_fact)


# In[17]:


import pandas as pd


# In[18]:


Mars_facts = pd.read_html(Mars_facts_url)
Mars_facts


# In[19]:


rights = list(Mars_facts[0][0])
lefts = list(Mars_facts[0][1])
mars_facts_df = pd.DataFrame ({'Name': rights,'Values':lefts})
mars_facts_df


# # Mars Hemispheres

# In[20]:


USGS_Astrogeology_url =  'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
base_USGS_URL = USGS_Astrogeology_url.split('gov/')[0]
browser.visit(USGS_Astrogeology_url)


# In[22]:


html = browser.html
soup =bs(html, 'html.parser')


# In[27]:


base_USGS_URL
visit_list = []
clicks = soup.find_all('a', class_='itemLink product-item')

for items in clicks:
    temps_st = base_USGS_URL+ str(items).split('href=')[1].split('>')[0].strip ('"')
    temps_st = temps_st.replace("//","/")
    if temps_st not in visit_list:
        visit_list.append (temps_st)
print (visit_list)


# In[28]:


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


# In[29]:


print (title_list)
print (img_url_list)


# In[30]:


hemisphere_image_urls = []
for i in range (len (img_url_list)):
    hemisphere_image_urls.append ({'title': title_list[i], 'img_url': img_url_list [i]})
    print (hemisphere_image_urls[i]['title'])
    print (hemisphere_image_urls[i]['img_url'] + '\n')
print (hemisphere_image_urls)


# In[ ]:




