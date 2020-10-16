import pymysql


db = pymysql.connect('192.168.153.128', 'root', 'root', 'Faker')
cursor = db.cursor()
cursor.execute('drop table if exists faker')
cursor.execute('''CREATE TABLE `faker` (
`姓名`  char (50) NOT NULL AUTO_INCREMENT ,
`年龄` INT (10) NOT NULL, 
`性别`  char (50) NOT NULL ,
`地区`  char (50) NOT NULL ,
`平均花费` char (50) NOT NULL ,
`出游距离` char (50) NOT NULL ,
`出游时间` char (50) NOT NULL ,
`出游频率` INT (10) NOT NULL ,
PRIMARY KEY (`姓名`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
''')
db.close()
