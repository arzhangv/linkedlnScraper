# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from LinkedlnScraper import LinkedlnScraper

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #Aditi's login
    email = "aditi.kotha03@gmail.com"
    password = "Arzhang19"
    #Arzhang's login
    '''email = "avaladkhani14@gmail.com"
    password = "Ukrzi7az$"'''
    "https://www.linkedin.com/checkpoint/challenge/AgE3kLbSJ8mj2AAAAYddM0ygrt7E_PxaaUs8N4kBi9NVnk7uKGD0lL1L6toPuXNSJmjWpc9X2OWTbVyssKYjhm7UfilfZw?ut=2P9oUXN4BiuqI1"
    #, "jr software engineer", "new grad software engineer"
    job_titles = ["entry level software engineer"]
    #, "Los Angles"
    locations = ["newport beach"]

    LinkedlnScraper = LinkedlnScraper(email, password, job_titles, locations)
    #LinkedlnScraper.scan_jobs()
    #LinkedlnScraper.extract_data_from_job_url()
    #LinkedlnScraper.connecting_to_mysqlDatabase()

    "data-topic-id=.*?data"
    url = 'https://www.linkedin.com/jobs/view/3574320799/?refId=Ipv0A5ER2%2FrQAjn4J%2BknWQ%3D%3D&trackingId=qwG%2FyT3Rw7k9lxZ1%2F66ZuQ%3D%3D&trk=flagship3_search_srp_jobs'
    words = url.split('/')
    print(words[5])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
