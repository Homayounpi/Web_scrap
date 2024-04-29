import re
import requests
from bs4 import BeautifulSoup


url = 'https://github.com/{}'
username= 'amirbigg'
r = requests.get(url.format(username),params={'tab':'repositories'})
content = BeautifulSoup(r.text,'html.parser')
repos_elements = content.find(id='user-repositories-list') 
repos = repos_elements.find_all('li')
for repo in repos:
    name = repo.find('h3').find('a').get_text(strip=True)
    language = repo.find(attrs={'itemprop':'programmingLanguage'})
    language = re.findall(r'>[a-zA-Z]+',str(language)) 
    language = str(language[0])[1:] if language else 'unknow'
    # language = language.get_text()
    stars = repo.find('a',attrs={'href':re.compile(r'\/stargazers')})
    stars = int(stars.get_text(strip=True)) if stars else 0
    print(name,language,stars)