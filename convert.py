import requests
from bs4 import BeautifulSoup as bs

r = requests.get('http://www.koeri.boun.edu.tr/scripts/lst0.asp')
soup = bs(r.content, 'html.parser')
pre = soup.select_one('pre').text

liste = [x.strip() for x in pre.split('\n')]
liste=liste[7:-2]
liste2=[]

for i in liste:
   liste2.append(list(filter(None,i.split(' '))))

