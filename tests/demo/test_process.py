


from threading import Lock, Thread
from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor

money = 0
lock = Lock()

def test_add_money():
    global money
    lock.acquire()
    print("before add: ", money)
    money += 100
    print("after add: ", money)
    lock.release()

def test_deduct_money():
    global money
    lock.acquire()
    print("before deduct: ", money)
    money -= 100
    print("after deduct: ", money)

# t1 = Thread(target=test_add_money).start()
# t2 = Thread(target=test_deduct_money).start()

p1 = Process(target=test_add_money).start()
p1 = Process(target=test_deduct_money).start()



