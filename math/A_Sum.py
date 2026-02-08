t = int(input())

for _ in range(t):
    x,y,z = map(int,input().split(" "))
    is_sum = False
    if y+z ==x or x+z == y or x+y ==z:
        is_sum = True
    if is_sum:
        print("YES")
    else:
        print("NO")