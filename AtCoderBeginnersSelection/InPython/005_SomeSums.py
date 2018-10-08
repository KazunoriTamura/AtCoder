N,A,B = input().split()
N = int(N)
A = int(A)
B = int(B)
answer = 0
for i in range(N):
    n = i + 1
    s = list(str(n))
    t = list(map(int,s))
    wa = sum(t)
    if A <= wa <= B:
        answer = answer + n
print(answer)