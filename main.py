import os
import math
import requests
import ascii
from config import place, unit
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

temp_unit = 'C' if unit=='metric' else 'F'
speed_unit = 'km/h' if unit=='metric' else 'mph'

url = f"http://api.openweathermap.org/data/2.5/weather?q={place}&units={unit}&appid={API_KEY}"
data = requests.get(url).json()

code = str(data['weather'][0]['id'])
if code[0]=='2':   art = ascii.thunderstorm
elif code[0]=='3': art = ascii.drizzle
elif code[0]=='5': art = ascii.rain
elif code[0]=='6': art = ascii.snow
elif code[0]=='7': art = ascii.atmosphere
elif code=='800':  art = ascii.clear
elif code[0]=='8': art = ascii.clouds

art = art.split('\n')

print(art[0], end=' ')
print()
print(art[1], end=' ')
print(f" {str(math.floor(data['main']['temp']))+'°'+temp_unit:<11}{'feels like '+str(math.floor(data['main']['feels_like']))+'°'+temp_unit:<40}")
print(art[2], end=' ')
print(f" {str(data['weather'][0]['main'].replace('Thunderstorm', 'Storm')):<11}{'wind '+str(data['wind']['speed'])+' '+speed_unit:<40}")
print(art[3], end=' ')
print(f" {datetime.utcfromtimestamp(data['dt']+data['timezone']).strftime('%I:%M %p'):<11}{data['name']+'/'+data['sys']['country']:<40}")
print(art[4], end=' ')