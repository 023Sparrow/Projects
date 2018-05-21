# Asks the user to enter a cost and either a country or state tax. It then returns the tax plus the total cost with tax.

def texcaculator(cost,taxrate):
    totalcost = cost*(1+taxrate)
    return totalcost

print('''
please input your tax rate:
''')
taxrate = float(input('>>>'))
print('''
please input your cost:
''')
cost = float(input('>>>'))
print('your total cost is {}'.format(texcaculator(cost,taxrate)))
