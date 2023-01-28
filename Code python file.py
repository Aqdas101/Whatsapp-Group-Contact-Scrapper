#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import csv
import re
import pandas as pd


# In[2]:


# Sukkur Shorthand & Typing
# Distric Sukkur
# TECHMA ZONE FAMILY
# Techmazone DS B13A
# STHP-2022 Preparation.
# Online Course Coupons
n = int(input('How many whatsapp group do you wanna scrap: '))
n = int(n)
groups = []
for i in range(0,n):
    name_group = input(" Enter group name: ")
    groups.append(name_group)


# In[3]:


driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Browser Driver.exe")
driver.get('https://web.whatsapp.com/')
driver.maximize_window()


# In[4]:


Groups = groups
variables = [re.sub(r"[^\w]", "" ,x) for x in groups]
for i,var in zip(Groups,variables):
    time.sleep(5)
    group_chat = WebDriverWait(driver, 360).until(
        EC.presence_of_element_located((By.XPATH, "//span[@title='{}']".format(i)))
        )
    group_chat.click()
    time.sleep(10)
    try:
        element = driver.find_element(By.XPATH,'//div[@data-testid="chat-subtitle"]/span')
        globals()[var] = element.text
    except StaleElementReferenceException:
        group_chat = WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.XPATH, "//span[@title='{}']".format(i)))
        )
        group_chat.click()
        element = driver.find_element(By.XPATH,'//div[@data-testid="chat-subtitle"]/span')
        time.sleep(10)
        globals()[var] = element.text       


# In[6]:


for i in variables:
    x = globals()[i]
    x = x.split(",")
    x = pd.Series(x)
    x = pd.DataFrame(x)
    x.to_csv('{}.csv'.format(i))


# In[ ]:




