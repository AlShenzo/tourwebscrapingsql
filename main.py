# request to get the page source codes
import requests
# selector lib extract the information we need
import selectorlib
import time
import sqlite3

connection = sqlite3.connect('data.db')


"INSERT INTO events VALUES('Tigers', 'Tiger City', '2088.10.14')"


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
    row = extracted.split(',')
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES (?,?,?)", row)
    connection.commit()

def read(extracted):
    row = extracted.split(',')
    row = [item.strip() for item in row]
    band,city,date = row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE band = ? AND city = ? AND date =?", (band,city,date))
    rows = cursor.fetchall()
    return rows

if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)

        if extracted!="No upcoming tours":
            row = read(extracted)
            if not row:
                store(extracted)
                send_email()
        time.sleep(2)