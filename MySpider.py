import csv,requests,re
from bs4 import BeautifulSoup

urlmode = 'https://www.v2ex.com/?tab='

urlorig = 'https://www.v2ex.com/?tab=all'
html = requests.get(urlorig).text
soup = BeautifulSoup(html, 'html.parser')
articles = []
for page in soup.find_all(class_='tab'):
    tab = re.findall(r'(?<=href="/\?tab=).+(?=">)', str(page))
    url = urlmode+tab[0]
    html = requests.get(url).text
    msoup = BeautifulSoup(html, 'html.parser')
    for article in msoup.find_all(class_='cell item'):
        title = article.find(class_='item_title').get_text().encode('utf-8').decode('utf-8', 'ignore')
        category = article.find(class_='node').get_text()
        author = re.findall(r'(?<=<a href="/member/).+(?="><img)', str(article))[0]
        u = article.select('.item_title > a')
        link = 'https://www.v2ex.com' + re.findall(r'(?<=href=").+(?=")', str(u))[0]
        articles.append([tab[0], title, category, author, link])

print(articles)
with open('v2ex.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['大标题', '文章标题', '分类', '作者', '文章地址'])
    for row in articles:
        writer.writerow(row)
