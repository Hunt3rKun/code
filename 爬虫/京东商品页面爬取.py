import requests

try:

    r = requests.get("https://item.jd.com/100006340761.html")
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print("爬取失败！")
