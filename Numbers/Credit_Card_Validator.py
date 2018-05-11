# Takes in a credit card number from a common credit card vendor (Visa, MasterCard, American Express, Discoverer) and validates it to make sure that it is a valid number (look into how credit cards use a checksum).

def verify_creditcard(n):
    creditlist = list(n)
    creditlist = [int(x) for x in creditlist]
    creditlist.reverse()
    j,odds,even,evens = 0,0,0,0
    for i in creditlist:
        j = j+1
        while (j+2)%2 == 1:
            odds = odds+i
        while (j+2)%2 == 0:
            even = i*2
            if even < 10:
                evens = evens + even
            else:
                even = (even%10) + (even//10)
                evens = evens + even
    creditnum = odds + evens
    if creditnum%10 == 0:
        return ('The credit card number is true.')
    else:
        return ('The credit card number is false.')

while True:
    print('please input your credit card number: ')
    num = input('>>>')
    print(verify_creditcard(num))