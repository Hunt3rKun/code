file = open("test.txt", "r")
fileadd = open("test2.txt", "r")
content = file.read()
contentadd = fileadd.read()
file.close()
fileadd.close()
content = content+contentadd
file = open("test2.txt", "w")
file.write(content)
file.close()