
while True:
    with open('grade.csv','a') as f:
        string = input("请输入学生信息，格式：姓名，性别，年龄，语文成绩，数学成绩，英语成绩\n")
        if string=='-1':
            break
        f.write(string)
        f.write('\n')
        f.close()

with open("grade.csv","r")as f1:
    txts=f1.readlines()
score= []
for i in txts:

    ls= i.strip('\n').split(',')
    score.append(ls)
score[0].append("sum")
for h in score[1:]:
    sum = int(h[3]) + int(h[4])+ int(h[5])
    h.append(str(sum))
score.sort (key = lambda X:X[6], reverse = True)
with open('statistics.csv','w') as fp:
    for h in score:
        for j in range(len(score[0])):
            fp.write(str(h[j]))
            fp.write(',')
        fp.write('\n')

