import requests

try:
    url = "https://www.sougo.com/tx?"
    kv1 = {'query':'python'}
    kv2 = {'User-agent':'mozilla/5.0'}
    r = requests.get(url,headers = kv2,params=kv1)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败!")