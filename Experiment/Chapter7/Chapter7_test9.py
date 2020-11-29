import re

iden = input("请输入手机号: ")
reg = "^(13[0-9]14[579]|15[0-3,5-9]|16[6]|17[0135678]|18[0-9]|19[89])\\d{8}$"    	#正则表达式.
reg = "/^[京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领A-Z]{1}[A-Z]{1}[A-Z0-9]{4}[A-Z0-9挂学警港澳]{1}$/"
pattern = re.compile(reg)
res = pattern.match(iden)
if res:
  print("您输入的手机号合法！")
else:
  print("手机号不合法。请重新输入！")