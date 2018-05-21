# The Factorial of a positive integer, n, is defined as the product of the sequence n, n-1, n-2, ...1 and the factorial of zero, 0, is defined as being 1. Solve this using both loops and recursion.
# recursion
def factoral(x):
    if x == 1:
        return 1
    else:
        return x*factoral(x-1)
print(factoral(5))
# loops
def factorial(x):
    sum = 1
    while x >= 1:
        sum = sum * x
        x = x-1
    return sum
print(factorial(5))
