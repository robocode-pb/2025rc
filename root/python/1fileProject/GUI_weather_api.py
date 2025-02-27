import customtkinter as ctk
import requests
import json

def get(name, url):
    response = requests.get(url).json()
    print(f'\n{name} = {json.dumps(response, indent=2)}')
    return response

def get_ip():
    return get('get_ip', f'https://api.ipify.org/?format=json')

def get_loc(ip):
    return get('get_loc', f'http://ip-api.com/json/{ip}')

def get_weather(lat, lon):
    return get('get_weather', 
               f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true')


def display_weather():
    ip = get_ip()
    loc = get_loc(ip['ip'])
    weather = get_weather(loc['lat'], loc['lon'])

    current_weather = {}
    for key, values in weather['current_weather_units'].items():
        current_weather[key] = f'{weather['current_weather'][key]} {values}'
    values = {**ip, **loc, **current_weather}

    text = ''
    for key in ('ip', 'regionName', 'time', 'temperature', 'windspeed', 'winddirection'):
        text += f'{key}: {values[key]}\n'
    weather_label.configure(text=text)

# Створення головного вікна
root = ctk.CTk()
root.geometry("250x200")
root.title("IP Wether")

bt = ctk.CTkButton(root, text="Update", command=display_weather)
bt.pack()

# Розміщення Label для виводу інформації про погоду
weather_label = ctk.CTkLabel(root, text="", justify="center")
weather_label.pack(pady=20)

display_weather()

# Запуск головного циклу
root.mainloop()
