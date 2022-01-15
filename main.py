# This is a sample Python script.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests


def print_hi(name):
    req = requests.get("https://missionprabhat.com/")
    soup = BeautifulSoup(req.content, "html.parser")

    res = soup.title

    print(res.get_text())



def facebook_login():
    options = Options()
    options.add_argument("user-data-dir=C:\\Users\\vinay\\AppData\\Local\\Google\\Chrome\\User Data")
    driver = webdriver.Chrome(executable_path=r'C:\\Users\\vinay\\Downloads\\chromedriver_win32\\chromedriver.exe', chrome_options=options)
    driver.get("https://docs.google.com/spreadsheets/d/1e5XMpCKyzxUHaRY_Ug6QZC_-epogJb3QMZS09GHBeJQ/edit#gid=0")




    time.sleep(900000)


if __name__ == '__main__':
    facebook_login()

