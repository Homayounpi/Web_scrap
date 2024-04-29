import requests
from bs4 import BeautifulSoup
import re


r = requests.get('https://news.ycombinator.com/')
articles = []
content = BeautifulSoup(r.text,'html.parser')
for item in content.find_all('tr',class_='athing'):
    item_a = item.find(class_='titleline').find('a')
    item_link = item_a.get('href') if item_a else None
    item_text = item_a.get_text(strip=True) if item_a else None 
    next_row = item.find_next_sibling('tr')

    item_score = str(next_row.find('span',class_='score'))
    item_score = re.findall(r'[0-9]+.points',item_score)
    item_score = item_score[0] if item_score else '0 point'
    # item_score = item_score.get_text(strip=True) if item_score else None 
    item_comments = next_row.find('a',text=re.compile(r'\d+(&nbsp;|\s)comments(s?)'))
    item_comments = item_comments.get_text(strip=True).replace('\xa0',' ') if item_comments else '0'
    articles.append({
        'link':item_link,
        'title':item_text,
        'score':item_score,
        'comment':item_comments
    })
for arti in articles:
    print(arti)





