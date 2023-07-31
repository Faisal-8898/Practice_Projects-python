import requests
import os
import json
if __name__ == '__main__':
    print("---Welcome to weather app---")
city = input ("Enter the name of city:\n")
url = f"https://api.weatherapi.com/v1/current.json?key=0dbfb8d1862a4c81ae761219233107&q={city}"
r = requests.get(url)
# wdic = json.loads(r.text);
# print(wdic)
wdic = r.json()
w = wdic["current"] ["temp_c"]
oscommand = f"say Current weather in {city} is {w}"
os.system(oscommand)
