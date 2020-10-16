import requests

try:
    url = "https://ip.cn/?ip="
    kv = {'ip': '117.11.42.125'}
    r = requests.get(url + '117.154.42.125')
    print(r.status_code)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print("爬取失败!")
