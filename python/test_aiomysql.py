import asyncio
from aiomysql import create_pool
import aiomysql
import time

@asyncio.coroutine
def asyncMysql(table):
    conn = yield from aiomysql.connect(host='localhost',
            user='root',
            password='d03724008',
            db='maria',
            port=3300,
            charset='utf8',
            loop=loop)

    cur = yield from conn.cursor()
    yield from cur.execute("SELECT * FROM `{}`".format(table))
    print(cur.description)
    r = yield from cur.fetchall()
    print(r)
    yield from cur.close()
    conn.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(test_example('ind'))

@asyncio.coroutine
def asyncTime():
    start = time.time()
    yield from asyncio.wait([
        # asyncMysql('ind'),
        # asyncMysql('test'),
        # asyncMysql('nmi'),
        asyncMysql('industry'),
        asyncMysql('industry1'),
        # asyncMysql('ind'),
    ])
    end = time.time()
    print('Complete in {} second(s)'.format(end-start))

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncTime())


import pymysql

def syncMysql(table):
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='d03724008',
                           db='maria',
                           port=3300,
                           charset='utf8'
                           )

    cur = conn.cursor()
    cur.execute("SELECT * FROM `{}`".format(table))
    print(cur.description)
    r = cur.fetchall()
    print(r)
    cur.close()
    conn.close()

def syncTime():
    start = time.time()
    syncMysql('industry')
    syncMysql('industry1')
    end = time.time()
    print('Complete in {} second(s)'.format(end-start))

syncTime()

# connction pool

async def go():
    start = time.time()
    async with create_pool(
            host='localhost',
            user='root',
            password='d03724008',
            db='maria',
            port=3300,
            charset='utf8',
            loop=loop) as pool:
        async with pool.get() as conn:
            async with conn.cursor() as cur:
                await cur.execute("SELECT * from `industry`;")
                value = await cur.fetchall()
                # print(value)
                await cur.execute("SELECT * from `industry1`;")
                value = await cur.fetchall()
                # print(value)
    end = time.time()
    print('Complete in {} second(s)'.format(end-start))

loop = asyncio.get_event_loop()
loop.run_until_complete(go())


def poolMysql(table):
    cur.execute("SELECT * FROM `{}`".format(table))
    print(cur.description)
    r = cur.fetchall()
    print(r)

async def poolTime():
    start = time.time()
    async with create_pool(
            host='localhost',
            user='root',
            password='d03724008',
            db='maria',
            port=3300,
            charset='utf8',
            loop=loop) as pool:
        async with pool.get() as conn:
            async with conn.cursor() as cur:
                await asyncio.wait([
                    poolMysql('industry'),
                    poolMysql('industry1'),
                ])
    end = time.time()
    print('Complete in {} second(s)'.format(end-start))

poolTime()
loop = asyncio.get_event_loop()
loop.run_until_complete(poolTime())

