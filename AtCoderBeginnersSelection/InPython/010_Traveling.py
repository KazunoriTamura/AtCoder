N = int(input())
plan = [input().split() for i in range(N)]

def check(t,z,memo={}):
    # 時刻tに(x,y)にいることは可能か？
    x = z[0]
    y = z[1]
    if (t,tuple(z)) in memo:
        return memo[(t,tuple(z))]
    elif ( abs(x) + abs(y) ) > t:
        flag = 0
    elif ( abs(x) + abs(y) ) == t:
        flag = 1
    elif t == 1:
        if x == 1 and y == 0:
            flag = 1
        elif x == 0 and y == 1:
            flag = 1
        elif x == -1 and y == 0:
            flag = 1
        elif x == 0 and y == -1:
            flag = 1
        else:
            flag = 0
    elif t == 2:
        if x == 2 and y == 0:
            flag = 1
        elif x == 1 and y == 1:
            flag = 1
        elif x == 0 and y == 2:
            flag = 1
        elif x == -1 and y == 1:
            flag = 1
        elif x == -2 and y == 0:
            flag = 1
        elif x == -1 and y == -1:
            flag = 1
        elif x == 0 and y == -2:
            flag = 1
        elif x == 1 and y == -1:
            flag = 1
        elif x == 0 and y == 0:
            flag = 1
        else:
            flag = 0
    else:
        flag2 = check(t-1,[x-1,y])
        if flag2:
            flag = 1
        else:
            flag3 = check(t-1,[x,y-1])
            if flag3:
                flag = 1
            else:
                flag4 = check(t-1,[x+1,y])
                if flag4:
                    flag = 1
                else:
                    flag5 = check(t-1,[x,y+1])
                    if flag5:
                        flag = 1
                    else:
                        flag = 0
    memo[(t,tuple(z))] = flag
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