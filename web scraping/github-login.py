import requests
from bs4 import BeautifulSoup
url = 'https://github.com/{}'
username = 'Homayounpi'
session = requests.Session()
r = session.get(url.format('login'))
countent = BeautifulSoup(r.text,'html.parser')
data = {}
for form in countent.find_all('form'):
    for inp in form.select('input[type=hidden]'):
        data[inp.get('name')] = inp.get('value')
data.update({'login':'user name','password:':'******'})
r = session.post(url.format('session'),data=data)
r = session.get(url.format(username))
content = BeautifulSoup(r.text,'html.parser')
user_info = content.find('span',class_='p-label')
print(user_info.get_text())
