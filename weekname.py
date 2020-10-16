weekname = "星期一星期二星期三星期四星期五星期六星期日"
weekid = int(input("请输入相应的数字："))
pos = (weekid-1)*3
print("相应的星期为：",weekname[pos:pos+3])
