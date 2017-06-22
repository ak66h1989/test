# from sqlite3 import *
import os
import time
from numpy import *
from pandas import *

os.chdir('C:\\Users\\ak66h_000\\Documents\\db\\')
# os.chdir('D:/')
conn = connect('mops.sqlite3')
c = conn.cursor()

id='5522'
companyId = "'{}'".format(id)
sql = "SELECT * FROM '{}' WHERE 公司代號 LIKE {}" .format('ifrs前後-綜合損益表', companyId)
inc = read_sql_query(sql, conn).replace('--', 'NaN')
table='ifrs前後-綜合損益表'
table='ifrs前後-綜合損益表'
table='ifrs前後-資產負債表-一般業'

import asyncio
import aioodbc


loop = asyncio.get_event_loop()


async def test_example():
    dsn = 'Driver=SQLite;Database=mysum.db'
    conn = await aioodbc.connect(dsn=dsn, loop=loop)

    cur = await conn.cursor()
    await cur.execute("SELECT * from forweb;")
    r = await cur.fetchall()
    print(r)
    await cur.close()
    await conn.close()

loop.run_until_complete(test_example())

