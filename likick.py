import requests
import sys
from bs4 import BeautifulSoup

def scrape():
    try:
        r = requests.get('https://www.li-kick.com/mix-match')
        soup = BeautifulSoup(r.text,'html.parser')

        site_data = []
        cards = soup.find(class_='material-card-grid').find_all(class_="material-card")
        for card in cards:
            temp_event = {}
            temp_event['subtitle'] = card.find(class_="material-card--subtitle").text
            temp_event['title'] = card.find(class_="material-card--title").text
            temp_event['date'] = card.find(class_="material-card--date").text
            temp_event['time'] = card.find(class_="material-card--time").text
            temp_event['location'] = card.find(class_="material-card--location").text
            temp_event['eventURL'] = "https://www.li-kick.com" + card.find(class_="material-card--footer").find("a").attrs['href']
            site_data.append(temp_event)

        print ("Succesfully Scraped " + str(len(site_data)) + " Events from Site")
        return site_data

    except Exception as e:
        print("[FAIL]: " + str(e))
        sys.exit()