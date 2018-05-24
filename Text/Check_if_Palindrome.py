def reversestr(s):
    so = ''
    s = list(s)
    s.reverse()
    for i in s:
        so = so + i
    return so

def if_palindrome(s):
    return s == reversestr(s)

print(if_palindrome('racecar'))
