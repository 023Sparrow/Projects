# Show addition, multiplication, negation, and inversion of complex numbers in separate functions. (Subtraction and division operations can be made with pairs of these operations.) Print the results for each operation tested.

def com_add(a,b,c,d):
    return ('{} + {}i'.format(a+b,c+d))
def com_sub(a,b,c,d):
    return ('{} + {}i'.format(a-c,b-d))
def com_muti(a,b,c,d):
    return ('{} + {}i'.format((a*c-b*d),(b*c+a*d)))
def com_div(a,b,c,d):
    return ('{} + {}i'.format(( (a*c+b*d)/c**2+d**2),((b*c-a*d)/(c**2+d**2))))


print(com_add(1,2,3,4))
print(com_sub(1,2,3,4))
print(com_muti(1,2,3,4))
print(com_div(1,2,3,4))
