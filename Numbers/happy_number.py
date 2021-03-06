# happy number
#A happy number is defined by the following process. Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers. Display an example of your output here. Find first 8 happy numbers.

def happy(num):
    past = set()
    while num != 1:
        num = sum(int(i)**2 for i in str(num))
        if num in past:
            return False
        past.add(num)
    return True
test = [x for x in range(500) if happy(x)][:8]
print(test)
