'''**Find e to the Nth Digit** - Just like the previous problem, but with e instead of PI. Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go.'''
import itertools
from decimal import Decimal, getcontext
from math import factorial as f
D = Decimal

def calc_e(n):
    getcontext().prec = n
    a = itertools.count(1)
    a = list(itertools.islice(a,0,1000))
    b = sum(map(lambda x: D(1)/D(f(x)), a))
    print(b)

print('请输入需要达到的 e 的小数位数。请勿超过5000位。')
while True:
    num = int(input('>>>'))
    if num < 1 or num > 5000:
        print('请重新输入')
        
    else:
        print('打印到 e 的第 %s 位小数:' % num)
        calc_e(num)
        break