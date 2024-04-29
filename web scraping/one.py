import requests
from bs4 import BeautifulSoup
import re

#-------------------------------------------------------------------------
# response = requests.get('https://en.wikipedia.org/wiki/Mao_Zedong')
# print(response)
# print(response.text)
# print(dir(response))
# print(response.reason)
#-------------------------------------------------------------------------
# response = requests.get('https://en.wikipedia.org/wiki/Mao_Zedong')
# content = BeautifulSoup(response.text,'html.parser')
# print(content)
# print(content.find('h1'))
# print(content.find('h1').attrs)
# print(content.find('h1').text)
# print(content.find_all('h2'))
# print(content.find_all(['h1','h2']))
# print(content.find(attrs={'role':'main'}))
# print(content.find_all(class_='mw-body-header vector-page-titlebar'))
# print(content.find_all('a',class_='mw-body-header vector-page-titlebar'))
# print(content.find_all(class_='mw-body-header vector-page-titlebar',limit=3))
# print(content.find('h1').get('id'))
# print(content.find(re.compile('^d')))
# print(content.select('li > a[title="Benjamin Tucker"]'))
#----------------------------------------------------------------------------------------

# url = 'https://bama.ir/'
# countent = requests.get(url=url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0'})
# print(countent.status_code)

#=================================================================================================
#send headers in dasty (lessen 8)
# r = requests.get('https://gitlab.com/',cookies={'':''})
# print(r.text)
#=================================================================================================



