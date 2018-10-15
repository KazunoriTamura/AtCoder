m = int(input())
if m < 100:
    vv = '00'
elif 100 <= m < 1000: 
    vv = '0'+str(m//100)
elif 1000 <= m <= 5000:
    vv = str(m//100)
elif 6000 <= m <= 30000:
    vv = str(round( m//1000 + 50 ))
elif 35000 <= m <= 70000:
    vv = str(round( ( m//1000 - 30 )//5 + 80 ) )
else:
    vv = '89'

print(vv)