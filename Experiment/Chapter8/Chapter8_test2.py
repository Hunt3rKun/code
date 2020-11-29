import re

iden = input("请输入车牌号: ")    	#正则表达式.
reg = "^[京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领A-Z]{1}[A-Z]{1}[A-Z0-9]{4}$"
pattern = re.compile(reg)
res = pattern.match(iden)
if res:
  print("您输入的车牌号合法！")
else:
  print("车牌号不合法。请重新输入！")