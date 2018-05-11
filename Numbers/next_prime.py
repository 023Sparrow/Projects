'''**下一个素数** - 让程序查找素数，直到用户选择停止请求下一个素数。'''
#!/usr/bin/python
# -*- coding: utf-8 -*-


def odd_numbers():#生成一个无限序列，由3开始的奇数
    i = 1
    while True:
        i = i + 2
        yield i
        
def ismuti(n):
    return lambda x: x % n > 0
    
def prime():
    yield 2
    it = odd_numbers()
    while True:
        n = next(it)
        yield n
        it = filter(ismuti(n), it)

for n in prime():
    print(n)