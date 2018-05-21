#**Collatz Conjecture** - Start with a number *n > 1*. Find the number of steps it takes to reach one using the following process: If *n* is even, divide it by 2. If *n* is odd, multiply it by 3 and add 1.

def collatz(n):
    k = 0
    while n != 1:
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n+1
        k = k+1
    return k

# test
print(collatz(5))
print(collatz(19))
print(collatz(2))
