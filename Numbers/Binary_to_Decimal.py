#**二进制到十进制和反向转换器**

#2 ---> 10
def BtoD(b):#参数为str格式便于列表化
    l = []
    for i in b:
        l.append(int(i))
    l.reverse()
    j,d,s = 0,0,0
    for i in l:
        d = i * (2**j)
        j = j+1
        s = s+d
    return s
'''test
print('请输入想要转换的二进制数: ')
b = input('>>>')
print(BtoD(b))'''
# 10 ---> 2
def DtoB(d):#参数为int格式
    l = []
    s = ''
    d = int(d)
    while d > 1:
        l.append(d % 2)
        d = d // 2
    l.append(1)
    l.reverse()
    for i in l:s = s + str(i)
    return s

# 选择计算模式
print('10进制转2进制，请输入1；2进制转10进制，请输入2；退出请输入0。')
while True:
    num = input('>>>')
    if num == '1':
        n = input('请输入想要转换的数字： ')
        print('{}的10进制转为2进制结果为 {}'.format(n,DtoB(n)))
    if num == '2':
        n = input('请输入想要转换的数字： ')
        print('{}的2进制转为10进制结果为 {}'.format(n,BtoD(n)))
    if num == '0':break