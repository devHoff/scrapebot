import requests

URL = "https://django-anuncios.solyd.com.br/automoveis/"

def search_cars(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(response.text)
            print("Response status code:", response.status_code)
        else:
            print("Error when requesting")
    except Exception as error:
        print("Error when requesting")
        print(error)

search_cars(URL)
