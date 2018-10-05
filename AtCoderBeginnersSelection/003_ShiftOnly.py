N = int(input())
A = []
A = A + input().split()
A = list(map(int,A))
count = 0
while 1:
    B = list(map(lambda x: x%2, A))
    num_odd = sum(B)
    if num_odd > 0:
        break
    else:
        A = list(map(lambda x: x/2, A))
        count = count + 1
print(count)