def reversestr(s):
    return s[::-1]

def if_palindrome(s):
    return s == reversestr(s)

print(if_palindrome('racecar'))
