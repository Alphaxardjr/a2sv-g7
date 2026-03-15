n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

p = 0
result = []

for x in b:
    while p < n and a[p] < x:
        p += 1
    result.append(p)

print(*result)
