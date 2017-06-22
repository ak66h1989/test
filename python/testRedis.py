  # ----import----
import redis
from pandas import *
from sqlite3 import *
import os
import time
from datetime import datetime, timedelta

starttime = datetime.now()

def timeDelta(s):
    global starttime
    finishtime = datetime.now()
    print(s,'timedelta: ', finishtime - starttime)
    starttime = finishtime

os.chdir('C:\\Users\\ak66h_000\\Documents\\db\\')
# os.chdir('D:/')
conn = connect('tse.sqlite3')
c = conn.cursor()

def mymerge(x, y):
    m = merge(x, y, on=[col for col in list(x) if col in list(y)], how='outer')
    return m

sql = "SELECT DISTINCT 證券代號 FROM '{}'".format('自營商買賣超彙總表 (股)')
dealId = read_sql_query(sql, conn)
dealId = dealId['證券代號'].tolist()
len(dealId)

import re
dealId = dealId['證券代號'].tolist()
dealId = [i for i in dealId if re.search('\D|^0', i) is None]


sql = "SELECT COUNT(*) FROM '%s'" % ('每日收盤行情(全部(不含權證、牛熊證))')
nrow = read_sql_query(sql, conn)[0]
r0 = nrow//2
sql = "SELECT * FROM '%s' WHERE 年月日 between '2004/02/11' and '2004/02/13'" % ('每日收盤行情(全部(不含權證、牛熊證))')

sql = "SELECT * FROM '{}' WHERE rowid between 1 and {}" .format('每日收盤行情(全部(不含權證、牛熊證))', r0)
df0 = read_sql_query(sql, conn)
df0
sql = "SELECT * FROM '{}' WHERE rowid between {} and {}" .format('每日收盤行情(全部(不含權證、牛熊證))', r0, nrow)
df1 = read_sql_query(sql, conn)
df1
df = mymerge(df0, df1)

df = DataFrame({ 'A' : 1.,'B' : Timestamp('20130102'),'C' : Series(1,index=list(range(4)),dtype='float32'),
'D' : np.array([3] * 4,dtype='int32'),'E' : Categorical(["test","train","test","train"]),'F' : 'foo' })
r = redis.StrictRedis(host='localhost', port=6379, db=0)
l=[1,2,3]
r.set('foo', l)
r.set('foo', df)
r.get('foo')
r.get('mykey')

df.serialize()
type()
str(r.get('foo'))
b=r.get('foo')
b.decode('utf-8')

r.set("key", df.to_msgpack(compress='zlib'))
r.get('key')
read_msgpack(r.get("key"))

sql="SELECT * FROM '{}' WHERE 證券代號 Like {}"
companyId = '5522'

close = read_sql_query(sql.format('每日收盤行情(全部(不含權證、牛熊證))', companyId), conn)
r.set("close:{}".format(companyId), close.to_msgpack(compress='zlib'))

value = read_sql_query(sql.format('個股日本益比、殖利率及股價淨值比', companyId), conn).drop(['證券名稱'], 1)
r.set("value:{}".format(companyId), value.to_msgpack(compress='zlib'))

margin = read_sql_query(sql.format('當日融券賣出與借券賣出成交量值(元)', companyId), conn)
r.set("margin:{}".format(companyId), margin.to_msgpack(compress='zlib'))

ins = read_sql_query(sql.format('三大法人買賣超日報(股)', companyId), conn)
r.set("ins:{}".format(companyId), ins.to_msgpack(compress='zlib'))

deal = read_sql_query(sql.format('自營商買賣超彙總表 (股)', companyId), conn).drop(['證券名稱'], 1).fillna(0)
r.set("deal:{}".format(companyId), deal.to_msgpack(compress='zlib'))

read_msgpack(r.get("deal:{}".format(companyId)))

sql="SELECT * FROM '%s'"
starttime = datetime.now()
df = read_sql_query(sql% ('三大法人買賣超日報(股)'), conn)
finishtime = datetime.now() - starttime
print(finishtime)
r.set("key", df.to_msgpack(compress='zlib'))
r.get('key')

sql = "SELECT COUNT(*) FROM '%s'" % ('每日收盤行情(全部(不含權證、牛熊證))')
nrow = read_sql_query(sql, conn)
nrow = nrow['COUNT(*)'][0]
r0 = nrow//2

starttime = datetime.now()
sql = "SELECT * FROM '{}' WHERE rowid between 1 and {}" .format('每日收盤行情(全部(不含權證、牛熊證))', r0)
df0 = read_sql_query(sql, conn)
sql = "SELECT * FROM '{}' WHERE rowid between {} and {}" .format('每日收盤行情(全部(不含權證、牛熊證))', r0, nrow)
df1 = read_sql_query(sql, conn)
finishtime0 = datetime.now() - starttime
print(finishtime0)
del df0, df1

starttime = datetime.now()
df=read_msgpack(r.get("key"))
finishtime1 = datetime.now() - starttime
print(finishtime1)
del df
finishtime.seconds
finishtime0/finishtime1

def func(a, b, c, d, e, f, g = 100):
    print(a, b, c, d, e, f, g)
f = curr(func)