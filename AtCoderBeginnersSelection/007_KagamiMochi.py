N = int(input())
a = []
for i in range(N):
    a.append(int(input()))

count = 0
while len(a) > 0:
    a_max = max(a)
    a.remove(a_max)
    count += 1
    while len(a) > 0 and max(a) == a_max:
        a.remove(a_max)

print(count)