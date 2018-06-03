# how how to spell out a number in English. You can use a preexisting implementation or roll your own, but you should support inputs up to at least one million (or the maximum value of your language's default bounded integer type, if that's less).

def nameofnum(x):
    if x == '1':return 'one'
    if x == '2':return 'two'
    if x == '3':return 'three'
    if x == '4':return 'four'
    if x == '5':return 'five'
    if x == '6':return 'six'
    if x == '7':return 'seven'
    if x == '8':return 'eight'
    if x == '9':return 'nine'
    if x == '.':return "dot"
    if x == '-':return 'negative'

def number_names(n):
    nameiter = map(nameofnum, str(n))
    return " ".join(nameiter)

print(number_names(-1154555555555556.185555555555555555555555548))
# 应该支持最多一百万个输入 没有做到 ，应该是string的长度限制问题。明天 请查 string 的长度限制 并解决
