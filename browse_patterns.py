import numpy as np
import time

# config - site roots

GOV_ROOT = "http://gov.edu/"
HONEYWELL_ROOT = "http://honeywell.edu/"
INTRANET_ROOT = "http://intra.zycron.edu/"
GITLAB_ROOT = "http://gitlab.zycron.edu/"

def rand_sleep():
    time.sleep(np.random.randint(3, 12)*np.random.rand()+1)

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
    driver.get(HONEYWELL_ROOT+"careers.html")
    rand_sleep()
    driver.get(HONEYWELL_ROOT+"careers/why-choose-honeywell.html")
    rand_sleep()
    driver.get(HONEYWELL_ROOT+"industrial.html")
    rand_sleep()
    driver.get(HONEYWELL_ROOT+"worldwide.html")
    rand_sleep()
    driver.get(HONEYWELL_ROOT+"buildings.html")
    rand_sleep()
    driver.get(HONEYWELL_ROOT+"hrdirect.html")
    rand_sleep()
    driver.get(HONEYWELL_ROOT+"newsroom.html")
    rand_sleep()
    driver.get(HONEYWELL_ROOT+"newsroom/news/2018/09/leap-into-quantum-computing.html")
    rand_sleep()
    driver.get(HONEYWELL_ROOT+"newsroom/news/2018/09/how-technology-is-keeping-schools-safe.html")
    rand_sleep()
    driver.get(HONEYWELL_ROOT)
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
    
    
