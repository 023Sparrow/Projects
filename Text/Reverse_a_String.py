def reversestr(s):
    s = list(s)
    s.reverse()
    return ''.join(s)
print('please input your string: ')
s = input('>>>')
print(reversestr(s))
