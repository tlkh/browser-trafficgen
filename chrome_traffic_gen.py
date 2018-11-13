import os
import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from browse_patterns import *

# main configuration
CHROME_HEADLESS = False
#CHROME_BINLOC = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
CHROMEDRIVER_BINLOC = "./chromedriver_linux"

GOV_ROOT = "file:///Users/timothy/Desktop/cybercity/govsg/index.html"

# initialise ChromeDriver

chrome_options = Options()
if CHROME_HEADLESS:
    chrome_options.add_argument("--headless")
#chrome_options.binary_location = CHROME_BINLOC

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_BINLOC, chrome_options=chrome_options)

# main event loop

while True:
    rand_sleep()
    browse_govsg(driver)
    rand_sleep()
    browse_honeywell(driver)
    rand_sleep()
    browse_intranet(driver)
    rand_sleep()
    browse_gitlab(driver)
