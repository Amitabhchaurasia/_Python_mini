from bs4 import BeautifulSoup
import requests
headers =  {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5)AppleWebKit/605.1.15 (KHTML, like Gecko)Version/12.1.1 Safari/605.1.15)'}
res=requests.get(f'https://fast.com/',headers=headers)
soup=BeautifulSoup(res.content,'html.parser')
speed=soup.select('#speed-value')[0].getText().strip()
unit=soup.select('#speed-units')[0].getText().strip()
print("***********NET*speed*********")
print(speed)