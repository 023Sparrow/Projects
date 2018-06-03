def count(w,s):
    countnum = 0
    for i in s:
        if i == w:
            countnum += 1
    return countnum

def countvowels(s):
    a = count('a',s)
    e = count('e',s)
    i = count('i',s)
    o = count('o',s)
    u = count('u',s)
    return a+e+i+o+u

testtext = 'vnaofnoaijnavavijfvapvnpofj'
print('''there are {} vowels in vnaofnoaijnavavijfvapvnpofj.
         {} a
         {} e
         {} i
         {} o
         {} u'''.format(countvowels(testtext),count('a',testtext),count('e',testtext),count('i',testtext),count('o',testtext),count('u',testtext)))
