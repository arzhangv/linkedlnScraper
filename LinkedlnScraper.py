import selenium
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from bs4 import BeautifulSoup as bs
import re as re
import time
import pandas as pd
from selenium.webdriver.common.by import By
import re
import urllib.parse

class LinkedlnScraper:



    email = ""
    password = ""
    job_titles = []
    locations = []

    def __init__(self, email, password, job_titles, locations):
        self.email = email
        self.password = password
        self.job_titles = job_titles
        self.locations = locations

    #setter abstracting linkedln for email account for security purposes
    def set_email(self):
        df = pd.read_csv("login_info.csv")
        self.email = df["email"][0]
    #setter abstracting linkedln for password account for security purposes

    def set_password(self):
        df = pd.read_csv("login_info.csv")
        self.password = df["password"][0]

    def create_url_query_for_24hrs(self, job, location, page):

        #base_url = "https://www.linkedin.com/jobs/search/"
        "https://www.linkedin.com/jobs/search/?currentJobId=3529577436&_TPR=r86400&keywords=entry%20level%20soaftware%20engineer&location=Unitied%20States&refresh=true&start=50"
        "https://www.linkedin.com/jobs/search/?currentJobId=3529577436&TPR=r86400&keywords=entry%20level%20soaftware%20engineer&location=Unitied%20States&refresh=true&start=25"

        ""
        base_url = "https://www.linkedin.com/jobs/search/?currentJobId=3529577436&f"
        total_url = base_url + f"_TPR=r86400&keywords={urllib.parse.quote(job)}&location={urllib.parse.quote(location)}&refresh=true&start=" + str(page)
        return total_url


    def parse_for_url_of_jobs(self, driver):

        #pass in the driver and create an array to hold the links  of all the Job URLs
        job_urls = []

        #get the raw HMTL to Parse
        html_content = driver.page_source
        soup = bs(html_content, "html.parser")

        #baseurl for linkedlin will concatenate later with remaining url for jobs
        base_url = "https://www.linkedin.com"


        #
        for link in soup.find_all('a'):

            if "/jobs/view/" in link.get('href'):

                totalURL = base_url+ link.get('href')
                job_urls.append(totalURL)


        return job_urls
        '''
        jobs_block = driver.find_element_by_class_name('jobs - search - results__list')
        jobs_list = jobs_block.find_elements(By.CSS_SELECTOR, '.jobs - search - results__list - item')
        for job in jobs_list:
            all_links = job.find_elements_by_tag_name('a')
            for a in all_links:

                if str(a.get_attribute('href')).startswith("https://www.linkedin.com/jobs/view") and a.get_attribute('href') not in job_urls:
                    job_urls.append(a.get_attribute('href'))
                    print(a.get_attribute('href'))

                else:
                    pass
        return job_urls'''


    def loginToLinkdln(self):

        PATH = "C:\Program Files (x86)\chromedriver.exe"
        self.set_email()
        self.set_password()
        driver = webdriver.Chrome(PATH)

        time.sleep(2)
        driver.get("https://www.linkedin.com/")
        time.sleep(2)


        #Obtain the email field by HTML name
        email_login= driver.find_element(By.XPATH,"/html/body/main/section[1]/div/div/form[1]/div[1]/div[1]/div/div/input")
        email_login.send_keys(self.email)

        # Obtain the password field by HTML name
        password_login= driver.find_element(By.XPATH,"/html/body/main/section[1]/div/div/form[1]/div[1]/div[2]/div/div/input")
        password_login.send_keys(self.password)

        login_button = driver.find_element(By.XPATH, "/html/body/main/section[1]/div/div/form[1]/div[2]/button")
        login_button.click()
        time.sleep(2)

        verification_page_url  = "https://www.linkedin.com/checkpoint/challenge/"
        if verification_page_url in driver.current_url:
            return False

        time.sleep(2)
        return driver

    def scan_jobs(self):
        driver = self.loginToLinkdln()
        driver.maximize_window()
        job_urls  = []
        #index for the webpage will increment by one everytime
        index = 0
        jobs_urls = []
        '''
        search_term = "entry level software engineer"
        location = "newport beach"
        base_url = "https://www.linkedin.com/jobs/search/"
        total_url = base_url + f"_&keywords={urllib.parse.quote(search_term)}&location={urllib.parse.quote(location)}&refresh=true&start=" + str(start)
        '''

        for job, location in zip( self.job_titles, self.locations):
            while index < 975:
                current_url = self.create_url_query_for_24hrs(job=job, location=location, page=index)
                try:
                    driver.get(current_url)
                    jobs_urls+=self.parse_for_url_of_jobs(driver)
                    print(len(jobs_urls))
                except TimeoutException:
                    print("URL doesn't exist")
                index += 25
                time.sleep(3)



        #driver.get(total_url)
        print(driver.current_url)
        #Anytime
        "https://www.linkedin.com/jobs/search/?currentJobId=3542661983&geoId=90000084&keywords=entry%20level%20software%20engineer&location=San%20Francisco%20Bay%20Area&refresh=true"
        #one week
        "https://www.linkedin.com/jobs/search/?currentJobId=3554277078&f_TPR=r604800&geoId=90000084&keywords=entry%20level%20software%20engineer&location=San%20Francisco%20Bay%20Area&refresh=true"
        #one month
        "https://www.linkedin.com/jobs/search/?currentJobId=3181163714&f_TPR=r2592000&geoId=90000084&keywords=entry%20level%20software%20engineer&location=San%20Francisco%20Bay%20Area&refresh=true"
        #24 hours
        "https://www.linkedin.com/jobs/search/?currentJobId=3560268022&f_TPR=r86400&keywords=entry%20level%20software%20engineer&location=San%20Francisco%20Bay%20Area&refresh=true"
        "https://www.linkedin.com/jobs/search/?currentJobId=3529577436&_TPR=r86400&keywords=entry%20level%20soaftware%20engineer&location=Unitied%20States&refresh=true&start=0"

        #Anytime on scraper
        "https://www.linkedin.com/jobs/search/?currentJobId=3529577436&_TPR=r86400&keywords=entry%20level%20soaftware%20engineer&location=Unitied%20States&refresh=true&start=0"
        try:
            "https://www.linkedin.com/jobs/search/?currentJobId=3560268022&f_TPR=r86400&geoId=90000084&keywords=entry%20level%20software%20engineer&location=San%20Francisco%20Bay%20Area&refresh=true"
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '''/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[3]/div/span/button'''))).click()

        except TimeoutException:
            print("button doesn't exist")


        time.sleep(60)


        driver.get("https://www.linkedin.com/uas/login")
        time.sleep(3)
        email = driver.find_element_by_id("username")
        email.send_keys(email)
        password = driver.find_element_by_id("password")
        password.send_keys(password)
        time.sleep(5)

