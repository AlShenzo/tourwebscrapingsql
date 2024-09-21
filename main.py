# request to get the page source codes
import requests
# selector lib extract the information we need
import selectorlib

import time

URL = 'https://programmer100.pythonanywhere.com/tours/'

def scrape(url):
    """ Scrape the page source from URL"""
    response = requests.get(url)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value

def send_email():
    print('Email was sent')

def store(extracted):
    with open('data.txt','a') as file:
        file.write(extracted +'\n')
def read(extracted):
    with open('data.txt','r')as file:
       return file.read()

if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        content = read(extracted)
        if extracted!="No upcoming tours":
            if extracted not in content:
                store(extracted)
                send_email(messages="Hey, a new event was found!")
        time.sleep(2)