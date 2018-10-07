N,Y = input().split()
# print(N,Y)
N = int(N)
Y = int(Y)

a_old = [int(N),0,0]
# print(a)

def check(a,Y):
    Z = 10000*a[0] + 5000*a[1] + 1000*a[2]
    # print(Z)
    if Z == Y:
        return 1
    else:
        return 0

def compute_part(a_new,Y):
    a_new_2 = [0,0,0]
    for i in range(a_new[1]+1):
        a_new_2[0] = a_new[0]
        a_new_2[1] = a_new[1] - i
        a_new_2[2] = a_new[2] + i
        # print(a_new_2)
        c = check(a_new_2,Y)
        # print(c)
        if c:
            a_answer = a_new_2
            flag = 1
            break
        else:
            a_answer = [-1,-1,-1]
            flag = 0
    return a_answer,flag

# flag = 0
a_answer = [-1,-1,-1]
a_new = [0,0,0]
for i in range(N+1):
    a_new[0] = a_old[0] - i
    a_new[1] = a_old[1] + i
    a_new[2] = a_old[2]
    a_answer,flag = compute_part(a_new,Y)
    if flag:
        break

# print(flag)
# print(a_answer)

if flag:
    print(a_answer[0],a_answer[1],a_answer[2])
else:
    print(-1,-1,-1)