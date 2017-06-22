# from multiprocessing import Pool
# import os, time, random
#
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(4):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')

# from multiprocessing import Process, Queue
# import os, time, random
#
# # 写数据进程执行的代码:
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
#
# # 读数据进程执行的代码:
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)
#
# if __name__=='__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()

from sqlite3 import *
import os
import time
from pandas import *
os.chdir('C:\\Users\\ak66h_000\\Documents\\db\\')
# os.chdir('D:/')
conn = connect('mops.sqlite3')
c = conn.cursor()

start = time.time()

id='5522'
companyId = "'{}'".format(id)
sql = "SELECT * FROM '{}' WHERE 公司代號 LIKE {}" .format('ifrs前後-綜合損益表', companyId)
inc = read_sql_query(sql, conn).replace('--', 'NaN')

from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    # time.sleep(3)
    q.put(inc)
    # time.sleep(random.random())


if __name__=='__main__':
    l=[]
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pw1 = Process(target=write, args=(q,))
    pw2 = Process(target=write, args=(q,))

    pw.start()
    pw1.start()
    pw2.start()
    l.append(q.get())
    l.append(q.get())
    l.append(q.get())
    # 等待pw结束:
    pw.join()
    pw1.join()
    pw2.join()
    print(l)
    end = time.time()
    print('Task runs %0.2f seconds.' % ((end - start)))

