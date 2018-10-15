def my_round(val, digit=0):
    p = 10 ** digit
    return (val * p * 2 + 1) // 2 / p

deg,dis = list(map(int,input().split()))
deg = deg/10
dis = my_round(dis/60,1)

n = int( ( deg - 11.25 ) // 22.5 )
n = n + 1

if n == 1:
    Dir = 'NNE'
elif n == 2:
    Dir = 'NE'
elif n == 3:
    Dir = 'ENE'
elif n == 4:
    Dir = 'E'
elif n == 5:
    Dir = 'ESE'
elif n == 6:
    Dir = 'SE'
elif n == 7:
    Dir = 'SSE'
elif n == 8:
    Dir = 'S'
elif n == 9:
    Dir = 'SSW'
elif n == 10:
    Dir = 'SW'
elif n == 11:
    Dir = 'WSW'
elif n == 12:
    Dir = 'W'
elif n == 13:
    Dir = 'WNW'
elif n == 14:
    Dir = 'NW'
elif n == 15:
    Dir = 'NNW'
else:
    Dir = 'N' 

if 0.0 <= dis <= 0.2:
    W = 0
elif 0.3 <= dis <= 1.5:
    W = 1
elif 1.6 <= dis <= 3.3:
    W = 2
elif 3.4 <= dis <= 5.4:
    W = 3
elif 5.5 <= dis <= 7.9:
    W = 4
elif 8.0 <= dis <= 10.7:
    W = 5
elif 10.8 <= dis <= 13.8:
    W= 6
elif 13.9 <= dis <= 17.1:
    W = 7
elif 17.2 <= dis <= 20.7:
    W = 8
elif 20.8 <= dis <= 24.4:
    W = 9
elif 24.5 <= dis <= 28.4:
    W = 10
elif 28.5 <= dis <= 32.6:
    W = 11
else:
    W = 12

if W == 0:
    Dir = 'C'

print(Dir,W)