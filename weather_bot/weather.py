from config import wthr_token
import requests
import json

def get_lat_lon(city):
    coord = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={wthr_token}')
    ans = {'lat' : coord.json()[0]['lat'], 'lon':  coord.json()[0]['lon']}
    return ans

def getweather (city):
    try:
        lat_lon = get_lat_lon(city)
        info = requests.get(f'http://api.openweathermap.org/data/3.0/onecall?lat={lat_lon['lat']}&lon={lat_lon['lon']}&appid={wthr_token}')
        return info     
    except:
        print("ты кого наебать пытаешься")

#print(get_lat_lon(input('пиши: ')))
print(getweather(input('пиши2: ')))




# with open("data.json", "w", encoding="UTF-8") as file_out:
#     json.dump(get_lat_lon('уварово'), file_out, ensure_ascii=False, indent=2)