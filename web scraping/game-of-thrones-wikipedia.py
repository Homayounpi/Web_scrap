import requests
from bs4 import BeautifulSoup


response = requests.get('https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes')
content = BeautifulSoup(response.text,'html.parser')
episodes = []
# ep_tables = content.find_all('table',class_='wikiepisodetable')
ep_tables = content.select('table.wikiepisodetable')
for table in ep_tables:
    headers = []
    rows = table.find_all('tr')
    for header in table.find('tr').find_all('th'):        
        headers.append(header.text)
    for row in table.find_all('tr')[1:]:
        values = []
        for cal in row.find_all(['th','td']):
            values.append(cal.text)
        if values:
            episodes_dict = {header[i]:values[i] for i in range(len(values)) }
            episodes.append(episodes_dict)
for ep in episodes:
    print(ep)
