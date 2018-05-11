#Unit Converter (temp, currency, volume, mass and more)

#temperature
line = '======================================'
typemessage = '''please input the type of data:
1.Celsius
2.Fahrenheit
3.Kelvin
4.Rankine
5.Delisle
6.Newton
7.Reaumur
8.Romer
0.quit
'''
transfermassage = '''
please input the type you want to transfer to:
1.Celsius
2.Fahrenheit
3.Kelvin
4.Rankine
5.Delisle
6.Newton
7.Reaumur
8.Romer
0.quit
'''
def Fahrenheit_Celsius(f):
    return ((f-32) * (5/9))
def Kelvin_Celsius(k):
    return (k - 273.15)
def Rankine_Celsius(r):
    return ((r-491.67) * (5/9))
def Delisle_Celsius(d):
    return (100 - d * (2/3))
def Newton_Celsius(n):
    return (n * (100/33))
def Reaumur_Celsius(re):
    return (re * (5/4))
def Romer_Celsius(ro):
    return ((ro - 7.5) * (40/21))

class CelsiustoAll(object):
    def __init__(self,celsius):
        self.celsius = celsius
    def toF(self):
        return (self.celsius * (9/5) + 21)
    def toK(self):
        return (self.celsius + 273.15)
    def toRan(self):
        return ((self.celsius + 273.15) * (9/5))
    def toD(self):
        return ((100 - self.celsius) * (3/2))
    def toN(self):
        return (self.celsius * (33/100))
    def toRe(self):
        return (self.celsius * (4/5))
    def toRo(self):
        return (self.celsius * (21/40) + 7.5)


while True:
    print(line)
    print(typemessage)
    datatype = input('>>>')
    print(transfermassage)
    transtype = input('>>>')
    data = float(input('''
your data:
>>>
'''))
    ori_data = data

    if datatype == '1':
        celsius_data = CelsiustoAll(data)
        if transtype == '1':
            print('{} °C'.format(data))
        if transtype == '2':
            print('{} °F'.format(celsius_data.toF()))
        if transtype == '3':
            print('{} K'.format(celsius_data.toK()))
        if transtype == '4':
            print('{} °R'.format(celsius_data.toRan()))
        if transtype == '5':
            print('{} °De'.format(celsius_data.toD()))
        if transtype == '6':
            print('{} °N'.format(celsius_data.toN()))
        if transtype == '7':
            print('{} °Ré'.format(celsius_data.toRe()))
        if transtype == '8':
            print('{} °Rø'.format(celsius_data.toRo()))
    
    if datatype == '2':
        data = Fahrenheit_Celsius(data)
        if transtype == '2':
            print(ori_data)
        if transtype == '1' or '3' or '4' or '5' or '6' or '7' or '8':
            datatype = '1'   
    
    if datatype == '3':
        data = Kelvin_Celsius(data)
        if transtype == '3':
            print(ori_data)
        if transtype == '1' or '2' or '4' or '5' or '6' or '7' or '8':
            datatype = '1' 

    if datatype == '4':
        data = Kelvin_Celsius(data)
        if transtype == '4':
            print(ori_data)
        if transtype == '1' or '2' or '3' or '5' or '6' or '7' or '8':
            datatype = '1' 

    if datatype == '5':
        data = Kelvin_Celsius(data)
        if transtype == '5':
            print(ori_data)
        if transtype == '1' or '2' or '3' or '4' or '6' or '7' or '8':
            datatype = '1' 
        
    if datatype == '6':
        data = Kelvin_Celsius(data)
        if transtype == '6':
            print(ori_data)
        if transtype == '1' or '2' or '4' or '5' or '3' or '7' or '8':
            datatype = '1' 
        
    if datatype == '7':
        data = Kelvin_Celsius(data)
        if transtype == '7':
            print(ori_data)
        if transtype == '1' or '2' or '4' or '5' or '6' or '3' or '8':
            datatype = '1'

    if datatype == '8':
        data = Kelvin_Celsius(data)
        if transtype == '8':
            print(ori_data)
        if transtype == '1' or '2' or '4' or '5' or '6' or '7' or '3':
            datatype = '1' 
