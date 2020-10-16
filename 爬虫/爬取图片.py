import requests
from fake_useragent import UserAgent
from lxml import etree

url = "http://img0.dili360.com/ga/M00/46/FC/wKgBy1iv0WmAaXa1AE7LkZQs2kI077.tub.jpg@!rw9"
response = requests.get(url, headers={"UserAgent": UserAgent().chrome})
e = etree.HTML(response.text)
img_urls = e.xpath('//article/img/@src')
print(img_urls)
for url in img_urls:
    response = requests.get(url, headers={"UserAgent": UserAgent().chrome})
    img_name = url[url.rfind(' /') + 1:]
    with open('img/' + img_name, 'wb')as f:
        f.write(response.content)
