import numpy as np
import time


def browse_govsg(driver):
    """Click around gov.sg site"""

    driver.get(GOV_ROOT)
    time.sleep(np.random.randint(1, 3))

    menu_button = driver.find_element_by_css_selector(
        "#homemenu_0_DivCode > ul > li:nth-child(6) > a")
    menu_button.click()

    time.sleep(np.random.randint(1, 3))

    listen_button = driver.find_element_by_css_selector(
        "#Body > div.introjs-tooltipReferenceLayer > div > div.introjs-tooltipbuttons > a")
    listen_button.click()

    time.sleep(np.random.randint(1, 3))

    factually = driver.find_element_by_css_selector(
        "#mainmenu_0_DivCode > ul > li:nth-child(4) > a")
    factually.click()

    time.sleep(np.random.randint(1, 3))

    driver.get(GOV_ROOT)
    time.sleep(np.random.randint(1, 3))

    hawker = driver.find_element_by_css_selector(
        "#homemenu_0_DivCode > ul > li:nth-child(7) > ul > li > a")
    hawker.click()

    time.sleep(np.random.randint(1, 3))
