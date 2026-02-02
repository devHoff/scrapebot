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

response = search_cars(URL)
if response:
    soap = parsing(response)