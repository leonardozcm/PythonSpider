import os,csv

path='D:\Stuffs\Your Dream\python\PythonSpider-master\coach'
files= os.listdir(path)

year_list=[]
for i in range(2008,2019):
    year=[]
    year_list.append(year)
"""From 2008"""
for file in files:
    with open(path+"\\"+file,"r", encoding='utf-8',newline='') as fr:
        rows=csv.reader(fr)
        for row in rows:
            if(len(row)<2 and row[1]==''):
                continue
            if(row[1].isdigit()):
              this_year=int(row[1])
              if(this_year>=2008 and this_year<=2018):
                year_list[this_year-2008].append(row)

print(year_list[0])

n=2008
for ye in  year_list:
    with open("D:\Year\\"+str(n)+".csv", 'w', encoding='utf-8',newline='') as f:
     writer = csv.writer(f)
     for row in ye:
        writer.writerow(row)
    n+=1