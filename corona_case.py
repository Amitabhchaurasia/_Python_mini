from bs4 import BeautifulSoup
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5)AppleWebKit/605.1.15 (KHTML, like Gecko)Version/12.1.1 Safari/605.1.15)'}
res= requests.get(f'https://www.mygov.in/covid-19/',headers=headers)
soup=BeautifulSoup(res.content,'html.parser')
ACTIVE_CASES= soup.select('.icount')[0].getText().strip() 
print("\t\t\t**************************")
print()
print("\t\t\t       ",ACTIVE_CASES)
print()
print("\t\t\t**************************")