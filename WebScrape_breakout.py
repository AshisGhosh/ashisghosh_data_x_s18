import requests
import bs4 as bs
import pandas as pd
import html5lib 

source = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.87158815800046&lon=-122.27274583799971",)
soup = bs.BeautifulSoup (source.content, features='html.parser')
# print (soup)
period = []
temp = []
desc = []
for forecast in soup.find_all(class_='forecast-tombstone'):
	# print(forecast.find(class_='period-name').text)
	# print(forecast.find(class_='temp').text)
	# print(forecast.find('img')['alt'])
	period.append(forecast.find(class_='period-name').text)
	temp.append(forecast.find(class_='temp').text)
	desc.append(forecast.find('img')['alt'])
print (period, temp, desc)
print (type(period))

dict1 = {'Period' : period, 'Temp': temp, 'Desc':desc}
df = pd.DataFrame(dict1)

print (df)

# dfs = pd.read_html(soup.find('ul',{'id':'seven-day-forecast-list'}))

# print(dfs)