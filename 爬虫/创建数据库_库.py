import pymysql
import re

#创建数据库
def create_database(database_name):
    db = pymysql.connect(
        host = '192.168.153.128',
        user = 'root',
        passwd = 'root'
    )
    cur = db.cursor()
    sql = 'create database if not exists {}'.format(database_name)
    cur.execute(sql)
    db.commit()
    db.close()
if __name__ == '__main__':
    database_name = 'Faker'
    create_database(database_name)