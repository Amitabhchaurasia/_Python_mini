from bs4 import BeautifulSoup
import requests
city=input("Enter the city which you want to find where ,it located : ")
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5)AppleWebKit/605.1.15 (KHTML, like Gecko)Version/12.1.1 Safari/605.1.15)'}
res = requests.get(f'https://www.google.com/search?q=weather+{city}',headers=headers)
soup=BeautifulSoup(res.content,'html.parser')
l=soup.select('#wob_loc')[0].getText().strip()
weather=soup.select('#wob_tm')[0].getText().strip()
time=soup.select('#wob_dts')[0].getText().strip()
st=soup.select('#wob_dc')[0].getText().strip()
print(l)
print(weather+"°C""   "+ st)
print(time)
