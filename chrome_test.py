import os  
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options

import time
import numpy as np

chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' 

driver = webdriver.Chrome(executable_path=os.path.abspath("/Users/timothy/chromedriver"),
                          chrome_options=chrome_options)

GOV_ROOT = "file:///Users/timothy/Desktop/cybercity/govsg/index.html"

while True:
    driver.get(GOV_ROOT)
    time.sleep(np.random.randint(1,3))

    menu_button = driver.find_element_by_css_selector("#homemenu_0_DivCode > ul > li:nth-child(6) > a")  
    menu_button.click()

    time.sleep(np.random.randint(1,3))

    listen_button = driver.find_element_by_css_selector("#Body > div.introjs-tooltipReferenceLayer > div > div.introjs-tooltipbuttons > a")
    listen_button.click()

    time.sleep(np.random.randint(1,3))

    articles = driver.find_element_by_css_selector("#content_1_DivCode > section > div > div.left > ul:nth-child(3) > li:nth-child(2) > a")  
    articles.click()  

    time.sleep(np.random.randint(1,3))

    articles = driver.find_element_by_css_selector("#content_1_DivCode > section > div > div.left > ul:nth-child(3) > li:nth-child(2) > a")  
    articles.click()

    time.sleep(np.random.randint(1,3))

    financial_aid = driver.find_element_by_css_selector("#content_1_DivCode > section > div > div.left > ul:nth-child(6) > li:nth-child(1) > a")  
    financial_aid.click()  

    time.sleep(np.random.randint(1,3))

    driver.get(GOV_ROOT)

    time.sleep(np.random.randint(1,3))

    factually = driver.find_element_by_css_selector("#homemenu_0_DivCode > ul > li:nth-child(4) > a")
    factually.click()

    time.sleep(np.random.randint(1,3))

    driver.get(GOV_ROOT)
    time.sleep(np.random.randint(1,3))

    hawker = driver.find_element_by_css_selector("#homemenu_0_DivCode > ul > li:nth-child(7) > ul > li > a")
    hawker.click()
    time.sleep(np.random.randint(1,3))
