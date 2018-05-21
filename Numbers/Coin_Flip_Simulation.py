# Write some code that simulates flipping a single coin however many times the user decides. The code should record the outcomes and count the number of tails and heads.
# 假设出现0为反面，1为正面

import random
def coinflip(n):
    coinlist = []
    for i in range(1,n):
        coinlist.append(random.randint(0,1))
    def is_zero(n):
        return n == 0
    zeros = list(filter(lambda x:x==0,coinlist))
    probability = len(zeros)/len(coinlist)
    return('出现反面的概率为：%.2f %%' % (probability*100))
# test

while True:
    print('please input the time you want to throw coins: ')
    num = int(input('>>>'))
    print(coinflip(num))