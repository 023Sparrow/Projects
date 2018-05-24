import re

def countword(s):
    it = re.finditer('\s', s)
    i = 1
    for match in it:
        i += 1
    return i

print(countword('this is a test sentence:If you want to locate a match anywhere in string, use search() instead (see also search() vs. match()).'))
