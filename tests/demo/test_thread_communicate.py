
from threading import Thread

import time

# 通过变量通信

# money = 0


# def add_money():
#     global money
#     print("money: ", money)
#     time.sleep(1)
#     money += 100
#     print("add_money: ", money)


# def deduct_money():
#     global money
#     print("money: ", money)
#     money -= 99
#     print("deduct_money: ", money)


# t1 = Thread(target=add_money)
# t2 = Thread(target=deduct_money)

# t1.start()
# t1.join()
# t2.start()


# 管道通信
from queue import Queue, LifoQueue, PriorityQueue

# Queue队列-先进先出

q = Queue()
q = LifoQueue()
q = PriorityQueue()

def producer():
    print("producer开始")
    for i,j in enumerate("我想你明媚"):
        print("producer put: ", (j,0 - int(i)))
        q.put((j,0 - int(i)))
    print("producer结束")

def consumer():
    print("consumer开始")
    for i in range(q.qsize()):
        print("consumer get: ", q.get())
    print("consumer结束")


t3 = Thread(target=producer)
t4 = Thread(target=consumer)

t3.start()
t3.join()
t4.start()

