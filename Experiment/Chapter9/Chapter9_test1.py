while True:
  str = input("请输入内容：")
  if str == '0':
    break
  with open("gch.txt","a") as fp:
    fp.write("\n")
    num = fp.write(str)

