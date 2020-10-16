dict = {'早餐': 10, '中餐': 15, '晚餐': 20, '零售': 15, '饮用水': 3}
for key in dict:
    print(str(key)+':'+str(dict[key]))
total = sum(value for key, value in dict.items())
print("费用总和：", total)
