import requests
def getHTMLText (ur1):
    try:
        r = requests.get(url)
        r.raise_for_status() #如果状态不是200,引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
            return "产生异常"
if __name__=="__main__":
        url = "http://www.baidu.com"
        print (getHTMLText (url))
