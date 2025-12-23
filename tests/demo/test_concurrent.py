

def test1():
    print("test1开始")
    print("test1结束")
    return True

def test2():
    print("test2开始")
    print("test2结束")
    return True

def test3():
    print("test3开始")
    print("test3结束")
    return True


# 线程两种方式: 继承Thread类、实现run方法, 直接使用Thread类

from threading import Thread

# 方式一：直接使用Thread类

# 分配线程
t1 = Thread(target=test1)
t2 = Thread(target=test2)
t3 = Thread(target=test3)

# 启动线程
t1.start()
t2.start()
t3.start()