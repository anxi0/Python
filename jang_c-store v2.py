from bs4 import BeautifulSoup
import requests as r
import os.path as o

brands = ['cu', 'gs25', 'seven', 'ministop', 'emart24']

def findpagelimit(brand): #send 100page and check the last page
    f=open("get.txt","w",encoding='utf-8')
    URL = "https://pyony.com/brands/" + brand + "/?page=100"
    start = "page-item active\"><a class=\"page-link\" href=\"?page="
    res = r.get(URL).text
    page = res[res.find(start)+len(start):]
    page = page[:page.find("</a>")]
    return page[0:2]

def readall(URL): #read the html of each page and read by bs4 div>strong tag
    html=r.get(URL).text
    bs = BeautifulSoup(html, 'html.parser')
    res = bs.select('div>strong')
    delete=['<strong>','</strong>','&amp;',' 손님 the guest,',' 현재 페이지 공유하기]',' 최근 게시글,',' 자유롭게 한마디,','[']
    for d in delete: #tag and korean dictionary deleting
        res=str(res).replace(d,'')
    return res

def beautifulize():
    f = open("list.txt", "r", encoding='utf-8')
    data = f.read()
    data=data.replace(",", "\n")
    print(data)
    f.close()

def number1_get():
    f=open("list.txt","w",encoding='utf-8')
    for i in brands: #brands loop
        limit = findpagelimit(i)  #founded last page
        f.write(i+',')
        for j in range(1,int(limit)+1): #all page loop
            URL = "https://pyony.com/brands/" + i + "/?page=" + str(j)
            f.write(str(readall(URL))) #file writing(brand+index)
            print(str(int(100*(j/int(limit))))+" percent done") #percentage
        print(i+" done")
    f.close()

def number2_read():
    if (o.exists("list.txt") != 1):
        print("No file!\n")
        print("Wait a sec I'm gonna make that.")
        number1_get()
    else:
        beautifulize()

while(1):
    print("Choose action\n1. get from net\n2. read file")
    passing = input(":")
    print(passing)
    if (int(passing) == 1): number1_get()
    elif (int(passing) == 2): number2_read()
    else:
        print("try again by number.")