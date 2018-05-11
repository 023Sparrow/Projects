'''
**Find PI to the Nth Digit** - Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.
输入一个数字，并使程序生成的 PI 达到小数位数。限制程序的执行范围。
'''
from decimal import Decimal
from decimal import getcontext

D = Decimal
# 高斯 - 勒让德算法
def Gauss_pi(n):
    getcontext().prec = n
    a,b,t,p = 1,1/D(2).sqrt(),1/D(4),1
    for i in range(1000):
        az = a
        a = (az+b)/2
        b = (az*b).sqrt()
        t = t - p*(a-az)**2
        p = 2 * p
        pii = (a+b)**2/(4*t)
    print(pii)
    return None

# π的莱布尼茨公式
import itertools
def Leibniz_pi(N):
    getcontext().prec = N
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    odds = itertools.count(1,2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    odd_N = list(itertools.islice(odds,0,N))
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    map(lambda a,b:4/D(a*b),odd_N,list(itertools.islice(itertools.cycle([1,-1]),0,N)))
    # step 4: 求和:
    result = sum(map(lambda a,b:4/D(a*b),odd_N,list(itertools.islice(itertools.cycle([1,-1]),0,N))))
    print(result)

# 楚德诺夫斯基算法
'''未完成OverflowError: (34, 'Result too large')'''
def Chudnovsky_pi(n):
    getcontext().prec = n
    from math import factorial as f
    s = D(0)
    for k in range(1000):
        s = s + D((((-1)**k * f(6*k) * 13591409+545140134*k) / (f(3*k) * f(k)**3 * 640320**(3*k+(3/2)))))
    pii = 1 / (12*s)
    print(pii)

print('请输入需要达到的 PI 的小数位数。请勿超过5000位。')
while True:
    num = int(input('>>>'))
    if num < 1 or num > 5000:
        print('请重新输入')
        
    else:
        print('打印到 PI 的第 %s 位小数:' % num)
        Gauss_pi(num)
        break