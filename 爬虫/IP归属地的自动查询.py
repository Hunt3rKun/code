import requests

try:
    url = "https://ip.cn/?ip="
    kv = {'ip': '47.96.237.181'}
    r = requests.get(url + '47.96.237.181')
    print(r.status_code)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print("爬取失败!")
