# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from LinkedlnScraper import LinkedlnScraper

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #Aditi's login
    email = 0
    password = 0

    #, "jr software engineer", "new grad software engineer"
    job_titles = ["entry level software engineer", "jr software engineer", "new grad software engineer"]
    #, "Los Angles"
    locations = ["United States, Los Angles, Orange County"]

    LinkedlnScraper = LinkedlnScraper(email, password, job_titles, locations)
    #LinkedlnScraper.scan_jobs()
    #LinkedlnScraper.extract_data_from_job_url()
    #LinkedlnScraper.connecting_to_mysqlDatabase()

    "data-topic-id=.*?data"
    #LinkedlnScraper.extract_data_from_job_url()
    LinkedlnScraper.soup_data()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
