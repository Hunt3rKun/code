scores = dict()
while True:
    print("==================欢迎进入学生管理系统====================")
    print("=======            1.添加学生成绩              =========")
    print("=======            2.修改学生成绩              =========")
    print("=======            3.删除学生成绩              =========")
    print("=======            4.查询学生成绩              =========")
    print("=======            5.统计学生成绩              =========")
    print("=======            6.退出管理系统              =========")
    print("======================================================")
    a = int(input("请输入你所要执行的功能："))
    if a == 1:
        id = int(input("请输入学生学号："))
        grade = int(input("请输入学生成绩："))
        scores[id] = grade
        print(scores)
        print("=============================================")
        print("========      1.继续添加学生信息     ==========")
        print("========      2.返回上一层          ==========")
        print("==============================================")
        b = int(input("请输入操作序号："))
        if b == 1:
            continue
        elif b == 2:
            continue
        else:
            print("请输入正确的序号！")
        continue
    if a == 2:
        id = int(input("请输入要修改成绩的学生学号："))
        grade = int(input("请输入修改后学生成绩："))
        scores[id] = grade
        print(scores)
        print("=============================================")
        print("========      1.继续修改学生成绩     ==========")
        print("========      2.返回上一层          ==========")
        print("==============================================")
        b = int(input("请输入序号："))
        if b == 2:
            continue
        elif b == a:
            continue
        else:
            print("请输入正确的序号！")
        continue
    if a == 3:
        id = int(input("请输入要删除成绩的学生学号："))
        del scores[id]
        print(scores)
        print("=============================================")
        print("========      1.继续删除学生成绩     ==========")
        print("========      2.返回上一层          ==========")
        print("==============================================")
        b = int(input("请输入序号："))
        if b == 1:
            continue
        elif b == 2:
            break
        else:
            print("请输入正确的序号！")
        continue
    if a == 4:
        id = int(input("请输入要查询的学生成绩的学号："))
        c = scores[id]
        print(scores)
        print("============================================")
        print("========      1.继续查询学生成绩     ==========")
        print("========      2.返回上一层          ==========")
        print("==============================================")
        b = int(input("请输入序号："))
        if b == 1:
            continue
        elif b == 2:
            break
        else:
            print("请输入正确的序号！")
        continue
    if a == 5:
        list = [scores.values()]
        print("最高分为%d。" % max(list))
        print("最低分为%d。" % min(list))
        print("学生平均成绩为%d." % (sum(list)/len(list)))
        print("=============================================")
        print("========      返回上一层           ==========")
        print("==============================================")
        continue
    if a == 6:
        print("已退出学生信息管理系统！")
        break
