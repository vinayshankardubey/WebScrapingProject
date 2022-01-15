# This is a sample Python script.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import numpy as np
import time
import pandas as pd
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def print_hi(name):
    req = requests.get("https://missionprabhat.com/")
    soup = BeautifulSoup(req.content, "html.parser")

    res = soup.title

    print(res.get_text())



def facebook_login():
    options = Options()
    options.add_argument("user-data-dir=C:\\Users\\vinay\\AppData\\Local\\Google\\Chrome\\User Data")
    driver = webdriver.Chrome(executable_path=r'C:\\Users\\vinay\\Downloads\\chromedriver_win32\\chromedriver.exe', chrome_options=options)
    driver.get("https://www.amarujala.com/")
    html_source = driver.page_source

    soup = BeautifulSoup(html_source, 'html.parser')


    heading_tags = ["h1", "h2", "h3"]

    lnks = []

    for tags in soup.find_all('a'):
        lnks.append(tags.get('href'))
    print(lnks)

    np.savetxt("shows.csv", lnks, delimiter=", ", fmt="% s")






if __name__ == '__main__':
    facebook_login()

