from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import random


def get_text_and_href():
    driver = webdriver.Firefox(executable_path='#path_to_geckodriver')
    wait = WebDriverWait(driver, random.randrange(1, 2) + random.random())  # reusable wait for random events
    url = 'page url'
    driver.get(url)
    # driver.implicitly_wait(2) 
    # or below choose the best for your situation. 
    wait.until(driver.find_element_by_css_selector('ul'))
    ul = driver.find_element_by_css_selector('ul')
    li = ul.find_elements_by_css_selector('li')
    list = []  # rename for your purpose
    for item in li:
        link = item.find_element_by_css_selector('a').get_attribute('href')
        # make an array of a 2D array with item text and link. 
        list.append([item.text, link])
    print(list)
