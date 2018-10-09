N = int(input())
D = list(map(int,[input() for i in range(N)]))
ans = len(set(D))
print(ans)