def piglatin(s):
    vowel = 'aeiou'
    if s[0] in 'aeiou':
        s = s + 'ay'
    else:
        s = s[1:] + s[0] + 'ay'
    return s
print(piglatin('apple'))
print(piglatin('balihe'))
