from faker import Faker  # 引入库

f = Faker(locale='zh_cn')  # 初始化

fileName = 'writePeopleData.txt'  # 准备写入的文件名
n = 0
while n < 300:  # 执行100次
    n += 1  # 每执行1次之后加1
    Name = f.name()  # 生成姓名
    date = f.date_between(start_date="-1y", end_date="now")  # 近一年随机日期
    age = f.random_int(min=30,max=50)  # 年龄
    cost = f.random_int(min=1200,max=5000)  #消费金额
    tra_number = f.random_int(min=0,max=10) #旅游次数
    area = f.province()
    way = f.boolean()
    fileContent = "%s" % Name, ',%s' % area,',%s' % date, ",%s" % age,',%s'% cost, ',%s' % tra_number ,',%s' % way + "\n"

    with open(fileName, 'a', encoding='gbk') as file:  # 追加写模式
        file.writelines(fileContent)

    print(fileContent)