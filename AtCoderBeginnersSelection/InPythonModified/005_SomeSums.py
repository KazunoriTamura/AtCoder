N,A,B = list(map(int,input().split()))
ans = 0
for i in range(N+1):
    I = str(i)
    J = list(I)
    K = list(map(int,J))
    S = sum(K)
    if A <= S <= B:
        ans += i
print(ans)