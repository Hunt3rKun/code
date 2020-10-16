import os
# -*- coding:utf-8 -*-
menus="""
1.添加学生成绩
2.修改学生成绩
3.删除学生信息
4.查询学生信息
5.统计所有学生信息
6.退出学生管理系统
"""
print("Python程序设计学生成绩管理系统")
student_inf={}
def add_student():
	while True:
		id=input("\t请输入学生学号：")
		if id in student_inf.keys():
			print("学号[%s]已存在！" %(id))
			continue
		else:
			score=input("\t请输入学生成绩：")
			student_inf[id] = score
			break

def update_student():
	id=input("\t请输入要修改学生学号：")
	if id not in student_inf.keys():
		print("不存在[%s]学号" % (id))
	else:
		score=input("\t请输入[%s]学号的学生成绩:" %(id))
		if len(score):
			student_inf[id] = score

def delete_student():
	id=input("\t请输入要删除的学生学号：")
	if id in student_inf.keys():
		del student_inf[id]
		print("学号[%s]学生信息已删除!" %(id))
	else:
		print("不存在[%s]学号" %(id))

def query_student():
	id = input("\t请输入要查询的学生学号：")
	if id in student_inf.keys():
		print('{:<20}{:<20}'.format(id, student_inf[id]), end='')

	else:
		print("不存在[%s]学号" % (id))
def traverse_student():
		print(student_inf)
while True:
	print(menus)
	num = input("请输入菜单编号:")
	if num.isdigit():
		if int(num) not in range(0,7):
			print("菜单编号输入错误，请重新输入!")
			continue
		else:
			if int(num)==1:
				add_student()
			elif int(num)==2:
				update_student()
			elif int(num)==3:
				delete_student()
			elif int(num)==4:
				query_student()
			elif int(num)==5:
				traverse_student()
			elif int(num)==6:
				os.system('cls')
			else:
				print("输入编号错误")
	else:
		print("请输入数字菜单编号")




