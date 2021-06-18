import requests

url = "https://www.google.com"

open_weatehr_url = 'https://pro.openweathermap.org/data/2.5/forecast/hourly?q={New York}&appid={25f4a11eb3d69176068be9cd63140f3e}'


def get_people_info():
    response = requests.get(open_weatehr_url)
    print(response.text)


get_people_info()