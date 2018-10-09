N = int(input())
A = list(map(int,input().split()))

A_sorted = sorted(A)

Alice = A_sorted[::-2]
Bob = A_sorted[-2::-2]
print( sum(Alice) - sum(Bob) )