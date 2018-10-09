# 二進数に直して考える
# 奇数なら右端のビットは1である
# 偶数なら右端のビットは0である
# 偶数のとき，2で割るたびに右シフトしていく
# 8÷2 = 4 は以下のようになる
# 1000 ---> 100
# 0が右端から何個あるかを数えていけばよい

N = int(input())
A = list(map(int,input().split()))
ans = []
for i in range(len(A)):
    a = bin(A[i])
    ans.append(len(a)-1-a.rfind('1'))
answer = min(ans)
print(answer)