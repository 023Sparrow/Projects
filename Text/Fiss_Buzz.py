# Fiss Buzz 1-100
def fissbuzz():
    fissbuzzlist = []
    for x in range(1,101):
        if x % 3 == 0:
            x = 'Fizz'
        elif x % 5 == 0:
            x = 'Buzz'
        elif x % 3 and x % 5 == 0:
            x = 'FizzBuzz'
        fissbuzzlist.append(x)
    return fissbuzzlist
print(fissbuzz())
