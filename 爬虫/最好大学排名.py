import requests
from bs4 import BeautifulSoup
import bs4


def gethtmltext(url): #获取网站HTML文本
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "爬取失败！"
def getlist(ulist,html):    #提取HTML文本中的关键信息
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[3].string])
    return ""
def printf(ulist,num):
    tplt = "{0:^6}\t{1:{3}^15}\t{2:^10}"            #定义槽模板
    print("{0:^6}\t{1:{3}^11}\t{2:^10}".format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))
    print("Sum：" + str(num))
def main():
    uinfo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
    html = gethtmltext(url)
    getlist(uinfo,html)
    printf(uinfo,25)        #打印25所大学的排名
main()