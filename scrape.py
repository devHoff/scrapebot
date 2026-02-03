import requests
from bs4 import BeautifulSoup

URL = "https://django-anuncios.solyd.com.br/automoveis/"

def search_cars(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print("Error when requesting")
    except Exception as error:
        print("Error when requesting")
        print(error)

def parsing(response_html):
    try:
        soup = BeautifulSoup(response_html, 'html.parser')
        return soup
    except Exception as error:
        print("Error when parsing")
        print(error)

def find_link(soup):
    cards_father = soup.find("div", class_="ui three doubling link cards")
    cards = cards_father.find_all("a")

    links = []
    for card in cards:
        links.append(card["href"])

    return links

response = search_cars(URL)
if response:
    soup = parsing(response)
    print(find_link(soup))



