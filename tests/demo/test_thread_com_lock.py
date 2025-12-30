
from threading import Lock, Thread
import time

from concurrent.futures import ThreadPoolExecutor

class BankAccount:


    def __init__(self) -> None:
        self.balance = 0
        self.lock = Lock()

    def deposit(self, amount):
        """存款"""
        print("添加存款: ", amount)
        self.lock.acquire()
        time.sleep(2)

        self.balance += amount
        print("存款后余额: ", self.balance)
        self.lock.release()

    def withdraw(self, amount):
        """取款"""
        print("取款: ", amount)
        self.lock.acquire()
        self.balance = self.balance - amount
        print("取款后余额: ", self.balance)
        # self.lock.release()


if __name__ == "__main__":
    b = BankAccount()
    # 线程方式
    # Thread(target=b.deposit, args=([2])).start()
    # Thread(target=b.withdraw, args=([2])).start()

    # 线程池方式
    t = ThreadPoolExecutor(max_workers=2)
    t.submit(b.deposit, 2)
    t.submit(b.withdraw, 2)
    