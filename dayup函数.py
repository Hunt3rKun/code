# 函数.py
def Dayup(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [0, 6]:
            dayup *= (1 - 0.01)
        else:
            dayup *= (1 + df)
    return dayup


dayfactor = 0.01
while Dayup(dayfactor) < 37.78:
    dayfactor += 0.001
print("工作日的努力参数为：{:.4f}".format(dayfactor))
