from bs4 import BeautifulSoup
import requests as r

brands = ['cu', 'gs25', 'seven', 'ministop', 'emart24']

def findpagelimit(brand):
    f=open("get.txt","w",encoding='utf-8')
    URL = "https://pyony.com/brands/" + brand + "/?page=100"
    start = "page-item active\"><a class=\"page-link\" href=\"?page="
    res = r.get(URL).text
    page = res[res.find(start)+len(start):]
    page = page[:page.find("</a>")]
    return page[0:2]

def readall(URL):
    html=r.get(URL).text
    bs = BeautifulSoup(html, 'html.parser')
    res = bs.select('div>strong')
    return res # a or w

f=open("list.txt","w",encoding='utf-8')
for i in brands:
    limit=findpagelimit(i)
    for j in range(1,int(limit)+1):
        URL = "https://pyony.com/brands/" + i + "/?page=" + str(j)
        f.write(str(readall(URL)))
        print(str(int(100*(j/int(limit))))+"percent done")
    print(i+" done")
f.close()