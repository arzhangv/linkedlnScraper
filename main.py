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
    job_titles = ["entry level soaftware engineer", "jr software engineer", "new grad software engineer"]
    locations = ["newport beach", "Los Angles"]

    LinkedlnScraper = LinkedlnScraper(email, password, job_titles, locations)
    LinkedlnScraper.scan_jobs()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
