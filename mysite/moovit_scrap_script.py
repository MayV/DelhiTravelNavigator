#
#prerequisite
#
#pip install bs4
#pip install urllib.request
#

from bs4 import BeautifulSoup
import urllib.request
import json

urls = [] #This list contains all the urls.

baseurl = r'https://moovitapp.com/index/en/'
tempurl = r'public_transit-lines-Delhi-1-3801-859237'
flag = True;
print(1);
while flag: 
    print(baseurl+tempurl)
    basepage = urllib.request.urlopen(baseurl+tempurl)
    basepage_html = BeautifulSoup(basepage,'html.parser')
    objList = basepage_html.find_all('li',class_="line-item")
    for item in objList:
        urls.append(item.a.get('href'))
    obj = basepage_html.find('a',class_="pagination-link next")
    if obj:
        tempurl = obj.get('href')
    else:
        flag = False
    
db_data = {}    #Contains complete data read by scrapping.

print(2)
for url in urls:
    print(baseurl+url)
    page = urllib.request.urlopen(baseurl+url)
    page_html = BeautifulSoup(page,'html.parser')
    obj = page_html.find('div', class_="line-number")
    objList = page_html.find_all('span',class_="stop-title")
    db_data[obj.text] = [item.text for item in objList]

with open('moovit_data.json','w') as file:
	file.write(json.dumps(db_data))
