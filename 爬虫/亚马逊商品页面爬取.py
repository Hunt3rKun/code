import requests

try:
    url = "https://www.amazon.cn/dp/B015P0A53Q?smid=A2EDK7H33M5FFG&ref_=Oct_CBBBCard_dsk_asin4&pf_rd_r=HJHK1C5TPP7AKEP3DJD7&pf_rd_p=5a0738df-7719-4914-81ee-278221dce082&pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-3"
    kv = {'User-agent': 'mozilla/5.0'}
    r = requests.get(url,headers = kv)
    print(r.request.headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print("爬取失败!")