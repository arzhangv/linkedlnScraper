# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import LinkedlnScraper


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    email = "aditi.kotha03@gmail.com"
    password = "Arzhang19"
    job_titles = ["entry level soaftwre engineer", "jr software engineer", "new grad software engineer"]
    locations = ["Unitied States"]

    LinkedlnScraper = LinkedlnScraper(email, password, job_titles, locations)
    LinkedlnScraper.loginToLinkdln()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
