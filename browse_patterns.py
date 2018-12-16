import numpy as np
import time

# config - site roots

GOV_ROOT = "http://gov.edu/"
HONEYWELL_ROOT = "http://honeywell.edu/"
INTRANET_ROOT = "http://intra.zycron.edu/"
GITLAB_ROOT = "http://gitlab.zycron.edu/"
CNA_ROOT = "http://channelnewsasia.edu/"
WIKI_ROOT = "http://wiki.zycron.edu/"

def rand_sleep():
    time.sleep(np.random.randint(5, 15)*np.random.rand()+1)

def browse_cna(driver):
    driver.get(CNA_ROOT)
    rand_sleep()
    driver.get(CNA_ROOT+"news/singapore/prime-minister-succession-ong-ye-kung-pap-cec-committee-10918764.html")
    rand_sleep()
    driver.get(CNA_ROOT+"news/singapore/singapore-invisible-people-in-class-conscious-society-10918552.html")
    rand_sleep()
    driver.get(CNA_ROOT+"news/asia/mother-malaysia-baby-dies-caretaker-husband-rape-10920150.html")
    rand_sleep()
    driver.get(CNA_ROOT+"news/business/self-driving-shuttle-bus-nus-trial-comfortdelgro-2019-10920352.html")
    rand_sleep()

def browse_wiki(driver):
    driver.get(WIKI_ROOT)
    rand_sleep()
    driver.get(WIKI_ROOT+"doku.php?id=start&do=index")
    rand_sleep()
    driver.get(WIKI_ROOT+"doku.php?id=start&do=login&sectok=")
    rand_sleep()

def browse_govsg(driver):
    driver.get(GOV_ROOT)
    rand_sleep()
    driver.get(GOV_ROOT+"news.html")
    rand_sleep()
    driver.get(GOV_ROOT+"news/from-the-media/oct-2018/page-1.html")
    rand_sleep()
    driver.get(GOV_ROOT+"news/this-week-at-gov/oct-2018/page-1.html")
    rand_sleep()
    driver.get(GOV_ROOT+"news/news/oct-2018/page-1.html")
    rand_sleep()
    driver.get(GOV_ROOT+"factually.html")
    rand_sleep()
    driver.get(GOV_ROOT+"factually/content/fake-sms-and-website-on-sg-bonus.html")
    rand_sleep()
    driver.get(GOV_ROOT+"factually/content/countering-radicalism-together.html")
    rand_sleep()
    driver.get(GOV_ROOT+"factually/content/does-our-prime-minister-get-paid-up-to-r.html")
    rand_sleep()
    driver.get(GOV_ROOT+"factually/environment.html#listing")
    rand_sleep()
    driver.get(GOV_ROOT+"factually/content/why-increase-water-prices.html")
    rand_sleep()
    driver.get(GOV_ROOT+"resources.html")
    rand_sleep()
    driver.get(GOV_ROOT+"resources/ecitizen/guides-and-tips-on-government-services.html")
    rand_sleep()
    driver.get(GOV_ROOT+"sgdi/ministries/index.html")
    rand_sleep()
    driver.get(GOV_ROOT+"contest/hawkercentres.html")
    rand_sleep()
    driver.get(GOV_ROOT+"sgdi/ministries/mewr.html")
    rand_sleep()
    driver.get(GOV_ROOT+"sgdi/ministries/pmo.html")
    rand_sleep()
    driver.get(GOV_ROOT+"microsites/everydropcounts.html")
    rand_sleep()
    driver.get(GOV_ROOT+"microsites/ndr2018.html")
    rand_sleep()
    driver.get(GOV_ROOT)
    rand_sleep()

def browse_honeywell(driver):
    driver.get(HONEYWELL_ROOT)
    rand_sleep()
    driver.get(HONEYWELL_ROOT+"www.honeywell.com/safety.html")
    rand_sleep()
    driver.get(HONEYWELL_ROOT+"investor.honeywell.com/index.html")
    rand_sleep()
    driver.get(HONEYWELL_ROOT+"investor.honeywell.com/file/Index5869.html?KeyFile=395705302")
    rand_sleep()
    driver.get(HONEYWELL_ROOT+"investor.honeywell.com/Cache/1500113911fb5d.pdf?KeyFile=1500113911")
    rand_sleep()
    driver.get(HONEYWELL_ROOT+"investor.honeywell.com/Cache/1500113912b329.pdf?KeyFile=1500113912")
    rand_sleep()
    driver.get(HONEYWELL_ROOT+"investor.honeywell.com/Cache/395407973.pdf?KeyFile=395407973&Output=3&OSID=9")
    rand_sleep()
    driver.get(HONEYWELL_ROOT+"www.honeywell.com/hrdirect.html")
    rand_sleep()
    driver.get(HONEYWELL_ROOT+"www.honeywell.com/industrial.html")
    rand_sleep()
    
def browse_intranet(driver):
    driver.get(INTRANET_ROOT)
    rand_sleep()
    driver.get(INTRANET_ROOT+"index.php/blog/")
    rand_sleep()
    driver.get(INTRANET_ROOT+"index.php/2018/11/08/annual_report_2018/")
    rand_sleep()
    driver.get(INTRANET_ROOT+"index.php/operations/")
    rand_sleep()
    driver.get(INTRANET_ROOT+"index.php/staff-services/")
    rand_sleep()
    driver.get(INTRANET_ROOT+"index.php/office-addresses-floor-plans-maps/")
    rand_sleep()
    driver.get(INTRANET_ROOT+"wp-admin")
    rand_sleep()
    driver.get(INTRANET_ROOT)
    rand_sleep()

def browse_gitlab(driver):
    driver.get(GITLAB_ROOT)
    rand_sleep()
    driver.get(GITLAB_ROOT+"users/password/new")
    rand_sleep()
    driver.get(GITLAB_ROOT)
    rand_sleep()
    
    
