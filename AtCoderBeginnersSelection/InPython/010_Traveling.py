N = int(input())
plan = [input().split() for i in range(N)]

def check(t,z):
    # 時刻tにz=(x,y)にいることは可能か？
    x = z[0]
    y = z[1]
    if ( abs(x) + abs(y) ) > t:
        flag = 0
    elif ( abs(x) + abs(y) ) == t:
        flag = 1
    else:
        for i in range(t//2+1):
            t_new = t - 2*i
            if ( abs(x) + abs(y) ) == t_new:
                flag = 1
            else:
                flag = 0
    return flag

for i in range(N):
    if i == 0:
        t = int(plan[i][0])
        z = [int(plan[i][1]),int(plan[i][2])]
        flag = check(t,z)
        if flag == 0:
            break
    else:
        t = int(plan[i][0]) - int(plan[i-1][0])
        z = [int(plan[i][1]) - int(plan[i-1][1]),int(plan[i][2]) - int(plan[i-1][2])]
        flag = check(t,z)
        if flag == 0:
            break

if flag:
    print('Yes')
else:
    print('No')