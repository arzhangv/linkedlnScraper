import selenium
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import mysql.connector
from datetime import date
import random
import pymysql
from selenium import webdriver
from bs4 import BeautifulSoup
import re as re
import time
import pandas as pd
from selenium.webdriver.common.by import By
import re
import urllib.parse
import csv
from csv import writer,reader
class LinkedlnScraper:



    email = ""
    password = ""
    job_titles = []
    locations = []
    df = pd.DataFrame
    def __init__(self, email, password, job_titles, locations):
        self.email = email
        self.password = password
        self.job_titles = job_titles
        self.locations = locations

    def connecting_to_mysqlDatabase(self, job_urls):
        #connect to Database
        db = pymysql.connect(host="linkedlnurls.cbnylc0eza1l.us-east-1.rds.amazonaws.com", user="arzhangv",
                             password="Ukrzi7az$")
        cursor = db.cursor()
        cursor.execute("select  version()")
        data = cursor.fetchone()
        sql = '''create database kTestDb'''


        cursor.execute(sql)
        cursor.connection.commit()

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
        #\
        base_url = "https://www.linkedin.com/jobs/search/?currentJobId=3529577436&f"
        total_url = base_url + f"_TPR=r86400&keywords={urllib.parse.quote(job)}&location={urllib.parse.quote(location)}&refresh=true&start=" + str(page)
        return total_url

    def check_exists_by_xpath(self, driver,xpath):
        try:
            driver.find_element(By.XPATH,xpath)
        except NoSuchElementException:
            return False
        return True
    def soup_data(self):
        driver = self.loginToLinkdln()
        driver.maximize_window()
        self.df = pd.read_csv("jobs_urls.csv")
        self.df.dropna()
        self.df.drop_duplicates()
        data = {
            "job_title": [],
            "job_description": [],
            "company": [],
            "location": [],
            "job_id": [],
            "url": [],
            "workplace_type": [],
            "date": []

        }
        today = date.today()
        for job in list(self.df["urls"]):
            driver.get(url)
            url = job
            rand_time = random.randint(2,8)
            time.sleep(rand_time)


            html_source = driver.page_source
            soup = BeautifulSoup(html_source,"html.parser")

            job_title = soup.find('h1', class_='t-24 t-bold jobs-unified-top-card__job-title').text

            body = soup.find('div',class_="jobs-box__html-content jobs-description-content__text t-14 t-normal jobs-description-content__text--stretch").text

            company = soup.find('a',class_="ember-view t-black t-normal").text

            location = soup.find('span',class_="jobs-unified-top-card__bullet").text

            workplace_type = soup.find('span', class_="jobs-unified-top-card__workplace-type").text

            words = url.split('/')
            job_id = words[5]

            data['job_title'].append(job_title)
            data['job_description'].append(body)
            data['company'].append(company)
            data['location'].append(location)
            data['workplace_type'].append(workplace_type)
            data['job_id'].append(job_id)
            data["date"].append(today)
        self.df.from_dict(data)
        self.df.to_csv("job_data.csv")



    def extract_data_from_job_url(self):
            #reading from csv and then cleaning up dataframe
            driver = self.loginToLinkdln()
            driver.maximize_window()
            self.df = pd.read_csv("jobs_urls.csv")
            self.df.dropna()
            self.df.drop_duplicates()
            data = {
                "job_title": [],
                "job_description": [],
                "company": [],
                "location": [],
                "job_id": [],
                "url": [],
                "workplace_type": [],
                "date": []

            }

            for job in list(self.df["urls"]):

                try:
                    driver.get(job)
                    time
                    time.sleep(3)
                except NoSuchElementException:
                    print("URL is not accessible")
                    continue

                html_content = driver.page_source
                BeautifulSoup(html_content,"html.parser")




                if self.check_exists_by_xpath(driver, '''//*[@id="ember32"]/span''') == True:
                    # Click on the show more to see the rest of the job posting

                    try:
                        button = driver.find_element(By.ID, '''ember31''')
                        button.click()
                    except ElementNotInteractableException:
                        print("button cannot be clicked!")
                        continue
                    soup = bs(driver.current_url)

                    #Getting the name of the comapny
                    try:
                        company = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div[1]/span[1]/span[1]").text
                    except NoSuchElementException:
                        print("company is not found")
                        company = "na"

                    # <span class="jobs-unified-top-card__subtitle-primary-grouping t-black">
                    #             <span class="jobs-unified-top-card__company-name">
                    #                   <a href="/company/vastspace/life/" id="ember149" class="ember-view t-black t-normal">
                    #                     VAST
                    #                   </a>
                    #             </span>
                    #               <span class="jobs-unified-top-card__bullet">
                    #                 Long Beach, CA
                    #               </span>
                    #
                    #               <span class="jobs-unified-top-card__workplace-type">On-site</span>
                    #           </span>


                    #Getting the location of the job from XPATH
                    location = driver.find_element(By.XPATH,  "/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div[1]/span[1]/span[2]").text
                    #https://www.linkedin.com/jobs/view/3566940281/?refId=Ipv0A5ER2%2FrQAjn4J%2BknWQ%3D%3D&trackingId=We9%2FuzItSMmT2vfAY%2BKslg%3D%3D&trk=flagship3_search_srp_jobs

                    #URL for the posting can be simply exracted from the list of job urls were iterating from
                    url = job

                    #Job id can be taken from the url
                    words = url.split('/')
                    job_id = words[5]

                    #Getting the name of the position from XPATH
                    job_title = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div[1]/h1').text

                    #Getting the job description from the XPATH
                    time.sleep(3)
                    #/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[2]/article/div/div[1]/span
                    try:

                        job_description = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[2]/article/div/div[1]/span").text
                    except NoSuchElementException:
                        job_description = "na"



                elif self.check_exists_by_xpath(driver,'''//*[@id="ember31"]/span''') == True:

                    button = driver.find_element(By.ID, '''ember31''')
                    button.click()

                    # Getting the name of the comapny
                    company = driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div[1]/span[1]/span[1]").text
                    # Getting the location of the job from XPATH
                    location = driver.find_element(By.XPATH,
                                                   "/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div[1]/span[1]/span[2]").text
                    # https://www.linkedin.com/jobs/view/3566940281/?refId=Ipv0A5ER2%2FrQAjn4J%2BknWQ%3D%3D&trackingId=We9%2FuzItSMmT2vfAY%2BKslg%3D%3D&trk=flagship3_search_srp_jobs

                    # URL for the posting can be simply exracted from the list of job urls were iterating from
                    url = job

                    # Job id can be taken from the url
                    words = url.split('/')
                    job_id = words[5]

                    # Getting the name of the position from XPATH
                    job_title = driver.find_element(By.XPATH,'/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div[1]/h1').text

                    # Getting the job description from the XPATH
                    time.sleep(3)
                    job_description = driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[4]/article/div/div[1]/span").text


                elif self.check_exists_by_xpath(driver, '''//*[@id="ember30"]/span''') == True:
                    button = driver.find_element(By.ID, '''ember31''')
                    button.click()
                    # Getting the name of the company
                    company = driver.find_element(By.XPATH,
                                                  "/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div[1]/span[1]/span[1]").text
                    # Getting the location of the job from XPATH
                    location = driver.find_element(By.XPATH,
                                                   "/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div[1]/span[1]/span[2]").text
                    # https://www.linkedin.com/jobs/view/3566940281/?refId=Ipv0A5ER2%2FrQAjn4J%2BknWQ%3D%3D&trackingId=We9%2FuzItSMmT2vfAY%2BKslg%3D%3D&trk=flagship3_search_srp_jobs

                    # URL for the posting can be simply exracted from the list of job urls were iterating from
                    url = job

                    # Job id can be taken from the url
                    words = url.split('/')
                    job_id = words[5]

                    # Getting the name of the position from XPATH
                    time.sleep(3)
                    job_title = driver.find_element(By.XPATH,'/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div[1]/h1').text

                    # Getting the job description from the XPATH
                    job_description = driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[4]/article/div/div[1]/span").text



    def parse_for_url_of_jobs(self, driver):

        #pass in the driver and create an array to hold the links  of all the Job URLs
        job_urls = []

        #get the raw HMTL to Parse
        html_content = driver.page_source
        soup = bs(html_content, "html.parser")

        #baseurl for linkedlin will concatenate later with remaining url for jobs
        base_url = "https://www.linkedin.com"

        #Iterate through all a tags
        for link in soup.find_all('a'):

            #narrow down a tags with href links connected to jobs
            if "/jobs/view/" in link.get('href'):
                #creating the total url = https://www.linkedin.com + job
                totalURL = str(base_url+ link.get('href'))
                job_urls.append(totalURL)
                print(totalURL)


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
        #returnining the previous driver page should be post login
        driver = self.loginToLinkdln()
        driver.maximize_window()

        #storing all the URLS found
        jobs_urls  = []
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
                    jobs_urls+= self.parse_for_url_of_jobs(driver)
                    print(len(jobs_urls))
                except TimeoutException:
                    print("URL doesn't exist")
                index += 25
                time.sleep(3)


        #rows = zip(jobs_urls)


        with open('jobs_urls.csv', 'w') as outfile:
            write = writer(outfile)
            for jobs in jobs_urls:
                write.writerow([jobs])
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







