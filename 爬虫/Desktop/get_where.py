import re
from time import sleep
from urllib.request import urlopen

import pandas as pd
import prettytable as pt
from bs4 import BeautifulSoup as bf
from selenium import webdriver

date,wter,wd_d,wd_g,wind_dire,wind = [],[],[],[],[],[]
#地址转id部分
#读取和转换部分
city_id = pd.read_excel('D:\桌面\Desktop\city_id.xlsx')
dict_c = city_id.set_index('City_CN').T.to_dict('list')
city = input('输入查询地：')
test_id = dict_c[city]
test_id.append("".join(filter(str.isdigit, test_id[0])))
print('城市ID：',test_id[1],sep='')

#爬虫部分
#爬取当日的天气
html_one="http://www.weather.com.cn/weather1d/"+test_id[1]+".shtml"
driver=webdriver.Firefox()
driver.get(html_one)
sleep(5)
page=bf(driver.page_source,'html5lib')
mes = page.find("div",{"class": 'sk'})
mes1 = mes.find("p",{"class": 'time'})
mes2 = mes.find("div",{"class": 'zs h'})
mes3 = mes.find("div",{"class": 'zs w'})
mes4 = mes.find("div",{"class": 'tem'})

time = mes1.span.get_text()
sd = mes2.em.get_text()
wind_dir = mes3.span.get_text()#风向
wind_pow = mes3.em.get_text()#风力
wd = mes4.span.get_text()

#爬取近七日的天气
html_dizhi = "http://www.weather.com.cn/weather/"+test_id[1]+".shtml"
html = urlopen(html_dizhi)
obj = bf(html.read(),'html.parser')
mes_links = obj.find_all("li", {"class": re.compile('sky skyid lv\d')})
for mes in mes_links:
    date.append(mes.h1.get_text())
    wter.append(mes.p.get_text())
    wd_g.append(mes.span.get_text())    
for i in range(7):
    wd_d.append(obj.select('.tem i')[i].get_text())
    wind.append(obj.select('.win i')[i].get_text())

#输出数据部分
tb_7 = pt.PrettyTable()
tb_7.field_names = ['日期','天气', '最高温度','最低温度','风力']

def seven_d():   
    for i in range(1,len(date)):
        tb_7.add_row([date[i], wter[i], wd_g[i],wd_d[i],wind[i]])
    print('******************************')
    print(city,'近七日天气',sep='')
    print(tb_7)

def one_d():
    print('------------------------------')
    print(city,'当日天气',sep='')
    print('更新时间：',time,sep='')
    print('相对湿度：',sd,sep='')
    print('风向/风力：',wind_dir,'/',wind_pow,sep='')
    print("当前温度：",wd,'℃',sep='')
    print('------------------------------')

while True:
    one_d()
    print("是否查看近七日天气？(y/n)")
    if input()=='y':
        seven_d()
        print('数据来源：中央气象台')
        break
    else:
        print('数据来源：中央气象台')
        break
