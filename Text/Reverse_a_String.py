def reversestr(s):
    so = ''
    s = list(s)
    s.reverse()
    for i in s:
        so = so + i
    return so

print('please input your string: ')
s = input('>>>')
print(reversestr(s))
