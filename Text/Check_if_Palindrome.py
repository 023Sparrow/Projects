def reversestr(s):
    s = list(s)
    s.reverse()
    return ''.join(s)

def if_palindrome(s):
    return s == reversestr(s)

print(if_palindrome('racecar'))
