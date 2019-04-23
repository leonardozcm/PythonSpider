import csv,requests,re
from bs4 import BeautifulSoup

def couch(url,name):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser').find('table',attrs={'class':'wikitable'})
    info = []
    if soup==None:
        return
    for coach in soup.find_all('tr'):
        coach_elem =re.split(r"[\n,–]",name+'\n'+coach.get_text())
        for ele in coach_elem:
            if(ele ==''):
                coach_elem.remove(ele)
        if(len(coach_elem)>2):
            info.append(coach_elem)
    with open(name+'.csv', 'w',errors='ignore',newline='') as f:
        writer = csv.writer(f)
        for row in info:
            print(row)
            writer.writerow(row)
    return

url='https://en.wikipedia.org/wiki/List_of_current_NCAA_Division_I_men%27s_basketball_coaches'
wikihead='https://en.wikipedia.org/'

html=requests.get(url).text
soup=BeautifulSoup(html,'html.parser').find('table',attrs={'class':'wikitable'})
coaches=[]
links=[]
'''print(table.find_all('tr')[1].get_text().split('\n'))'''
for coach in soup.find_all('tr'):
  coach_elem=coach.get_text().split('\n')
  link=coach.find('span',attrs={'class':'fn'})
  if link!=None :
      url_name=link.find('a').get('href')


      links.append([url_name,url_name.split('/')[2]])
      print(link.find('a').get('href'))
  coaches.append(coach_elem)

print(links)

with open('FBS.csv', 'w', encoding='utf-8',newline='') as f:
    writer = csv.writer(f)
    for row in coaches:
        writer.writerow(row)

counter=1
for coach in links:
    couch(wikihead+coach[0],coach[1])
    counter+=1
    if(counter>20):
        break

