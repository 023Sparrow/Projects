# _*_ conding:utf-8 _*_
from math import sqrt as s
def fib(n):
    x = ((1+s(5))/2)**n
    y = ((1-s(5))/2)**n
    a = (s(5)/5) * (x - y)
    return int(a)

print('请输入希望生成的第 n 个数字的斐波那契数列。按 Ctrl + C 退出')
while True:
    num = int(input('>>>'))
    l = []
    for i in range(num):
        l.append(fib(i))
    print(l)