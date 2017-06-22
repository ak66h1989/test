import pymysql

# Connect to the database
conn = pymysql.connect(host='localhost',
                           user='root',
                           password='d03724008',
                           db='maria',
                           port=3300,
                            charset='utf8'
                           )


cur = conn.cursor()

#--cannot use chinese table and column name--

# cur.execute('SET NAMES big5')
# sql = '''
# CREATE TABLE `當日融券賣出與借券賣出成交量值` (
#     `年月日` varchar(255) ,
#     `證券名稱` varchar(255) ,
#     `融券賣出成交數量` varchar(255) ,
#      `融券賣出成交金額` varchar(255) ,
#       `借券賣出成交數量` varchar(255) ,
#        `借券賣出成交金額` varchar(255)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
#
# '''

# sql = '''
# CREATE TABLE `users` (
#     `id` int(11) NOT NULL AUTO_INCREMENT,
#     `email` varchar(255) COLLATE utf8_bin NOT NULL,
#     `password` varchar(255) COLLATE utf8_bin NOT NULL,
#     PRIMARY KEY (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
# AUTO_INCREMENT=1
# '''

sql = "SELECT * from `industry`;"

cur.execute(sql)
conn.commit()
print(cur.description)

print()

for row in cur:
    print(row)






# ----import----
from sqlite3 import *
import os
import time

os.chdir('C:\\Users\\ak66h_000\\Documents\\db\\')

# insert data to sqlite
conn = connect('test.sqlite3')
c = conn.cursor()
sql = "SELECT * from `industry`;"
df.to_sql(name='industry', con=conn)

# test read data from sqlite
start = time.time()
conn = connect('test.sqlite3')
df = read_sql(sql, conn)
end = time.time()
print('Complete in {} second(s)'.format(end - start))

# test read data from mysql by pandas
start = time.time()
conn = pymysql.connect(host='localhost',
                           user='root',
                           password='d03724008',
                           db='maria',
                           port=3300,
                            charset='utf8'
                           )
df = read_sql(sql, conn)
end = time.time()
print('Complete in {} second(s)'.format(end - start))

# test read data from mysql by pymysql
start = time.time()
conn = pymysql.connect(host='localhost',
                           user='root',
                           password='d03724008',
                           db='maria',
                           port=3300,
                            charset='utf8'
                           )
cur = conn.cursor()
cur.execute(sql)
conn.commit()
end = time.time()
print('Complete in {} second(s)'.format(end - start))

# ----result----
# read data drom sqlite is very quick while from mysql is very slow