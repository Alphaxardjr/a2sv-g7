t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split(" ")))
    a.sort()
    min_value = a[0]
    max_value = a[-1]
    if abs(min_value - max_value) <= 1:
        print("YES")
    else:
        print("NO")

possible = True
for i in range(1, n):
    if a[i] - a[i-1] > 1:
        possible = False
        break
print("YES" if possible else "NO")
