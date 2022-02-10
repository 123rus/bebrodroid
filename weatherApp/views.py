from django.http import HttpResponse
from django.shortcuts import render
import requests

# Create your views here.

def main(request):
    # city = request.POST.get('city')
    return render(request, "main.html")

def search(request):
    if request.method == 'POST':
        API_key = 'ca47be775bcdce04caa140c563a84b6d'
        city = request.POST.get('city')
        API = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_key}'
        data = requests.get(API).json()
        coord = data['main']['temp']
        flike = data['main']['feels_like']
        min_temp = data['main']['temp_min']
        max_temp = data['main']['temp_max']
        weather=f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@4x.png"
        return render(request, 'main.html', {'data' :data, 'city':city.title(), "coord":coord, "flike":flike, "min_temp":min_temp, "max_temp":max_temp, "weather":weather})