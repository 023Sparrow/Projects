# Sieve of Eratosthenes

def odd_numbers():#生成一个无限序列，由3开始的奇数
    i = 1
    while True:
        i = i + 2
        yield i
def ismuti(n):
    return lambda x: x % n > 0
def eratosthenes():
    yield 2
    it = odd_numbers()
    while True:
        n = next(it)
        yield n
        it = filter(ismuti(n), it)

for n in eratosthenes():
    print(n)
