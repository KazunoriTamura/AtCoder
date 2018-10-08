N = int(input())
a = []
a = list(map(int,input().split()))
alice = 0
bob = 0
for i in range(N):
    if i%2 == 0:
        a_max = max(a)
        # print(a_max)
        alice += int(a_max)
        index = a.index(a_max)
        # print(index)
        del a[index]
    else:
        a_max = max(a)
        bob += int(a_max)
        # print(a_max)
        index = a.index(a_max)
        # print(index)
        del a[index]
sa = alice - bob
print(sa)