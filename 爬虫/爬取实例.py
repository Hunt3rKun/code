import requests

def gethtmltext(url,):
    try:
        kv = {'User-agent': 'mozilla/5.0'}
        r = requests.get(url,headers = kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text)
    except:
        print("error!")
def main():
    url = 'https://s.taobao.com/search?q=荣耀V20'
    gethtmltext(url)
main()