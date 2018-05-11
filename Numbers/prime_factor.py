# _*_ utf-8 _*_
#**质因数分解** - 让用户输入一个数字，找到所有质因数 (如果有的话) 并显示它们。
#生成 n 以内质数,包括n本身
def eratosthenes(n):
    a = list()
    temp = [True] * (n+1)
    for i in range(2, n+1):
        if (temp[i]):
            j = i * i
            while (j <= n):
                temp[j] = False
                j = j + i
                
    for i in range(2, n+1):
        if (temp[i]):
            a.append(i)
    return a
  
# 质因数分解
def primefac(n):
  l = []
  n_ori = n
  for i in eratosthenes(n):
    while n%i == 0:
      l.append(i)
      n = n/i
  
  if l[0] == n_ori:
      print("该数为质数。")
  else:
      print(l)

while True:
    print("请输入数字：")
    num = int(input(">>>"))
    primefac(num)