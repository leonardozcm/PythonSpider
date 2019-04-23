import csv, requests, re
from bs4 import BeautifulSoup

url_head = 'http://cs.hust.edu.cn/szdw/szll'
url_tear = '.htm'
url_tab = ['', '/8', '/7', '/6', '/5', '/4', '/3', '/2', '/1']
# url_tab = ['']
teachers_links = []
teachers = []

for tab in url_tab:
    html = requests.get(url_head + tab + url_tear)
    html.encoding='utf-8'
    soup = BeautifulSoup(html.text, 'html.parser').find_all('tr', attrs={'class': 'tr-box'})
    for professor in soup:
        link = professor.find('a').get('href')
        if link != '#' and link != 'javascript:void(0)':
            teacher_name = professor.find('a').string
            teachers_links.append([teacher_name, link])

praise_head='http://faculty.hust.edu.cn/system/resource/tsites/praise.jsp?teacherid='
praise_tear='&apptype=index&ac=getPraise'

fail_count=0
print('failed at '+fail_count.__str__())
for link in teachers_links:
     html = requests.get(link[1])
     html.encoding='utf-8'
     soup=BeautifulSoup(html.text,'html.parser')
     pattern = re.compile(r"'teacherid':(.*?),'homepageid'", re.MULTILINE | re.DOTALL)
     script = pattern.findall(html.text)
     if(len(script)==0):
        fail_count+=1
        continue
     praise_link=praise_head+script[0]+praise_tear
     json=requests.post(praise_link)
     praise=re.split('[:}]',json.text)[1]
     print(link[0]+':'+praise+' ,'+link[1])
     teachers.append([link[0],int(praise),link[1]])

print('failed at '+fail_count.__str__())
teachers=sorted(teachers, key =lambda teacher:teacher[1], reverse=False)
with open('TL.csv', 'w',encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for row in teachers:
        writer.writerow(row)
