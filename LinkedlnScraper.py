from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import re as re
import time
import pandas as pd
class LinkedlnScraper:
    email = ""
    password = ""
    job_titles = ["entry level soaftwre engineer", "jr software engineer", "new grad software engineer"]
    locations = ["Unitied States"]

    def __init__(self, email, password, job_titles):
        self.email = email
        self.password = password
        self.job_titles = job_titles

    def loginToLinkdln(self):
        PATH = "C:\Program Files (x86)\chromedriver.exe"

        driver = webdriver.Chrome(PATH)
        driver.get("https://www.linkedin.com/uas/login")
        time.sleep(3)
        email = driver.find_element_by_id("username")
        email.send_keys(email)
        password = driver.find_element_by_id("password")
        password.send_keys(password)
        time.sleep(5)
