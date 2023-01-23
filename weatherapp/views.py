from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import re
# Create your views here.

def get_html_content(city):
    USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    city = city.replace(" ", "+")
    html_content = session.get(f'https://www.google.com/search?q=weather+in+{city}').text
    return html_content



def get_weather(request):
    weather_data = None
    if 'city' in request.GET:
        city = request.GET.get('city')
        html_content = get_html_content(city)
        soup = BeautifulSoup(html_content,'html.parser')
        weather_data=dict()
        weather_data['region']=soup.find('div',attrs={'id':'wob_loc'}).text
        weather_data['datetime']=soup.find('div',attrs={'id':'wob_dts'}).text
        weather_data['status']=soup.find('span',attrs={'id':'wob_dc'}).text
        weather_data['humidity']=soup.find('span',attrs={'id':'wob_hm'}).text
        weather_data['wind']=soup.find('span',attrs={'id':'wob_ws'}).text
        weather_data['temp']=soup.find('span',attrs={'id':'wob_tm'}).text
        img=soup.find('img',attrs={'id':'wob_tci'})
        weather_data['img']=img['src']

    return render(request,"weather.html",{'weather':weather_data})

