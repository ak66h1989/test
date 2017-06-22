import asyncio
import time
time.sleep(1)

urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']

async def call_url(url):
    print('Starting {}'.format(url))
    response = await print(url)
    data = await print(url+1)
    print('{}: {} bytes: {}'.format(url, len(data), data))
    return data

futures = [call_url(url) for url in urls]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))


async def my_coroutine():
    start = time.time()
    await asyncio.sleep(1)
    await asyncio.sleep(1)
    await asyncio.sleep(1)
    end = time.time()
    print('Complete in {} second(s)'.format(end-start))

tasks = [
    my_coroutine(),
    my_coroutine(),
    my_coroutine(),
    my_coroutine()]

loop = asyncio.get_event_loop()
start = time.time()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print('Complete in total {} second(s)'.format(end-start))

@asyncio.coroutine
def my_coroutine(task_name, seconds_to_sleep=3):
    print('{0} sleeping for: {1} seconds'.format(task_name, seconds_to_sleep))
    yield from asyncio.sleep(seconds_to_sleep)
    print('{0} is finished'.format(task_name))


loop = asyncio.get_event_loop()
tasks = [
    my_coroutine('task1', 4),
    my_coroutine('task2', 3),
    my_coroutine('task3', 2)]
loop.run_until_complete(asyncio.wait(tasks))


async def sleeptime(t):
    time.sleep(t)


async def my_coroutine(task_name, seconds_to_sleep=3):
    print('{0} sleeping for: {1} seconds'.format(task_name, seconds_to_sleep))
    await sleeptime(seconds_to_sleep)
    print('{0} is finished'.format(task_name))


loop = asyncio.get_event_loop()
tasks = [
    my_coroutine('task1', 4),
    my_coroutine('task2', 3),
    my_coroutine('task3', 2)]
loop.run_until_complete(asyncio.wait(tasks))


import asyncio

urls = [0, 1, 2, 3]

def f(x):
    print(x*(-1))
    return x


async def call_url(url):
    response = await f(url)
    print(response*(-1))
    data = response
    return data

futures = [call_url(url) for url in urls]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))


async def slow_operation(n):
    print(n)
    await asyncio.sleep(n)
    print("Slow operation {} complete".format(n))


async def main():
    start = time.time()
    await asyncio.wait([
        slow_operation(3),
        slow_operation(1),
        slow_operation(2),
    ])
    end = time.time()
    print('Complete in {} second(s)'.format(end-start))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print(1)

import time
import asyncio

@asyncio.coroutine
def slow_operation(n):
    print("begin: {} ".format(n))
    yield from asyncio.sleep(n)
    print("Slow operation {} complete".format(n))
    return n


@asyncio.coroutine
def main():
    start = time.time()
    x = yield from asyncio.wait([
        slow_operation(2),
        slow_operation(3),
        slow_operation(1),
    ])
    end = time.time()
    print('Complete in {} second(s)'.format(end-start))
    return x

loop = asyncio.get_event_loop()
finished, unfinished = loop.run_until_complete(main())
for task in finished:
    print(task.result())


from sqlite3 import *
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

@asyncio.coroutine
def slow_operation(table):
    x = yield from read_sql_query("SELECT * FROM '{}' WHERE 公司代號 LIKE {}".format(table, companyId), conn)
    print("Slow operation {} complete".format(table))
    return x

async def asyncSleep(t):
    await time.sleep(t)

@asyncio.coroutine
def slow_operation(table):
    x = read_sql_query("SELECT * FROM '{}' WHERE 公司代號 LIKE {}".format(table, companyId), conn)
    yield from asyncSleep(1)
    print("Slow operation {} complete".format(table))
    return x

@asyncio.coroutine
def main():
    start = time.time()
    x = yield from asyncio.wait([
        slow_operation('ifrs前後-綜合損益表'),
        slow_operation('ifrs前後-資產負債表-一般業'),
        slow_operation('ifrs前後-綜合損益表'),
    ])
    end = time.time()
    print('Complete in {} second(s)'.format(end-start))
    return x

loop = asyncio.get_event_loop()
finished, unfinished = loop.run_until_complete(main())
finished = list(finished)
for task in finished:
    print(task.result())

finished[0].result()
finished[1].result()
finished[2].result()

def sf(table):
    x = read_sql_query("SELECT * FROM '{}' WHERE 公司代號 LIKE {}".format(table, companyId), conn)
    time.sleep(1)
    print("Slow operation {} complete".format(table))
    return x

start = time.time()
sf('ifrs前後-綜合損益表')
sf('ifrs前後-資產負債表-一般業')
sf('ifrs前後-綜合損益表')
end = time.time()
print('Complete in {} second(s)'.format(end-start))



async def sf(x):
    return x

async def sf():
    df = read_sql_query(sql, conn)
    print(df)
    return df

async def af():
    x = await sf()
    print(x)
loop.run_until_complete(af())

@asyncio.coroutine
def main():
    start = time.time()
    yield from asyncio.wait([
        sf(),
        sf(),
        sf(),
    ])
    end = time.time()
    print('Complete in {} second(s)'.format(end-start))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

import asyncio

async def slow_operation(future):
    await asyncio.sleep(1)
    future.set_result('Future is done!')

def got_result(future):
    print(future.result())
    loop.stop()

loop = asyncio.get_event_loop()
future = asyncio.Future()
asyncio.ensure_future(slow_operation(future))
future.add_done_callback(got_result)
loop.run_forever()

