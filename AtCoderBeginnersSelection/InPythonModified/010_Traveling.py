N = int(input())
plan = [input().split() for i in range(N)]
flag = 0
for i in range(N):
    t = int(plan[i][0])
    x = int(plan[i][1])
    y = int(plan[i][2])
    if ( x + y ) > t:
        flag = 0
        break
    elif ( x + y ) == t:
        flag = 1
    else:
        if ( x + y + t ) % 2 == 0:  # x＋yとtの偶奇が一致
            flag = 1
        else:   # x＋yとtの偶奇が一致せず
            flag = 0
            break
if flag:
    print('Yes')
else:
    print('No')