import csv,requests,re
from bs4 import BeautifulSoup

def couch(url,name):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser').find('table',attrs={'class':'wikitable'})
    info = []
    print(soup.find_all('tr')[0].get_text())
    for coach in soup.find_all('tr'):
        coach_elem = coach.get_text().split('\n')
        for ele in coach_elem:
            if(ele ==''):
                coach_elem.remove(ele)
        info.append(coach_elem)
    with open(name+'.csv', 'w',encoding='utf-8') as f:
        writer = csv.writer(f)
        for row in info:
            writer.writerow(row)

"""couch('https://en.wikipedia.org/wiki/Chris_Collins_(basketball)','Chris Collins')"""