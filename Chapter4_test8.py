dict = {'早餐': 10, '中餐': 15, '晚餐': 20, '其他': 15}
for key in dict:
    print(str(key)+':'+str(dict[key]))
total = sum(value for key, value in dict.items())
print("费用总和：", total)
