



def add(a, b):
    print("加加加")
    return a + b

def sub(a, b):
    print("减减减")
    return a - b


input("请输入任意键结束, 如果是a则是加，是s便士减")
a, b = input("请输入两个数字，以空格分隔: ").split()
a, b = int(a), int(b)
