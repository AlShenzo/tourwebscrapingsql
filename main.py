# request to get the page source codes
import requests
# selector lib extract the information we need
import selectorlib

URL = 'https://programmer100.pythonanywhere.com/tours/'

def scrape(url):
    """ Scrape the page source from URL"""
    response = requests.get(url)
    source = response.text
    return source


if __name__ == "__main__":
    print(scrape(URL))