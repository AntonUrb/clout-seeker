import time

import requests
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def fname_checker(firstname, lastname):
    driver = uc.Chrome(headless=True, use_subprocess=False)
    url = f"https://www.fastpeoplesearch.com/name/{firstname}-{lastname}"
    driver.get(url)
    time.sleep(2)
    try:
        driver.find_element(By.CSS_SELECTOR, "button[aria-label='Consent']").click()
    except NoSuchElementException:
        pass
    bs = BeautifulSoup(driver.page_source, "html.parser")
    address_fulltext = bs.select_one(".card strong").text
    splitted_address = address_fulltext.split("\n")
    phone_nr = bs.select(".card strong")[3].text.strip()
    driver.quit()
    final_str = f"""First name: {firstname}
Last name: {lastname}
Address: {splitted_address[0]} {splitted_address[1]}
Number: +1 {phone_nr}"""
    return final_str
