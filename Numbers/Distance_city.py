# Calculates the distance between two cities and allows the user to specify a unit of distance. This program may require finding coordinates for the cities like latitude and longitude.   
# image the earth is a sphere
from math import cos as cos
from math import sin as sin
from math import asin as asin
from math import acos as acos
from math import pi as pi

def distance(alongitude,alatitude,blongitude,blatitude):
    alongitude = (pi/180)*alongitude
    alatitude = (pi/180)*alatitude
    blatitude = (pi/180)*blatitude
    blongitude = (pi/180)*blongitude
    s = 6371*acos(cos(alatitude)*cos(blatitude)*cos(alongitude-blongitude)+sin(alatitude)*sin(blatitude))
    return s

while True:
    alongitude = float(input('''
    情输入城市A的经度：
    >>>'''))
    alatitude = float(input('''
    情输入城市A的纬度：
    >>>'''))
    blongitude = float(input('''
    情输入城市B的经度：
    >>>'''))
    blatitude = float(input('''
    情输入城市B的纬度：
    >>>'''))
    if alongitude or alatitude or blongitude or blatitude > 180:
        print('数值不对，请重新输入。')
    else:
        unitnum = input('''请输入希望的到的距离单位: 
        1.米
        2.千米
        3.英里
        4.里
        >>>''')
        kmdistance = distance(alongitude,alatitude,blongitude,blatitude)
        if unitnum == '1':
            print('{} m'.format(kmdistance*1000))
        if unitnum == '2':
            print('{} km'.format(kmdistance))
        if unitnum == '3':
            print('{} mile'.format(kmdistance*1.609344))
        if unitnum == '4':
            print('{} 里'.format())
