N,Y = input().split()
# print(N,Y)

a = [int(N),0,0]
# print(a)

def check(a,Y):
    Z = 10000*a[0] + 5000*a[1] + 1000*a[2]
    if Y == Z:
        return 1
    else:
        return 0

flag = 0
for i in range(N):
    N_new = N - i
    a[0] = N_new
    if check(a,Y):
        flag = 1
        break

if flag:
    return a

flag2 = 0
for i in range()