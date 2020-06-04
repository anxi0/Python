from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import parse

f = open("locations.txt", "r", encoding="utf-8")
f2 = open('result.txt',"w",encoding="utf-8")
lines = f.readlines()
for locate in lines:
    f2.write(locate)
    url = parse.urlparse("https://m.map.kakao.com/actions/searchView?q=" + str(locate)) 
    query = parse.parse_qs(url.query)
    send="https://m.map.kakao.com/actions/searchView?"+parse.urlencode(query, doseq=True)
    res=urlopen(send)
    soup=BeautifulSoup(res,'html.parser')
    f2.write(soup.select('#placeList > li:nth-child(1) > a.link_result > span > span.txt_g')[0].text+"\n")