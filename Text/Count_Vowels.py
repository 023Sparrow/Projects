def count(w,s):
    countnum = 0
    for i in s:
        if i == w:
            countnum += 1
    return countnum

def countvowels(s):
    counta = count('a',s)
    counte = count('e',s)
    counti = count('i',s)
    counto = count('o',s)
    countu = count('u',s)
    return counta+counte+counti+counto+countu

testtext = 'vnaofnoaijnavavijfvapvnpofj'
print('''there are {} vowels in testtext.
         {} a
         {} e
         {} i
         {} o
         {} u'''.format(countvowels(testtext),count('a',testtext),count('e',testtext),count('i',testtext),count('o',testtext),count('u',testtext)))
