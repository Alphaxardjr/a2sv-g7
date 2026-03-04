# 

t = int(input())
mx = 0
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split(" ")))
    count = True
    for i in range(n):
        turn = max(a)
        if turn >= mx:
            a.insert(a.index(turn),0)
            mx = turn 
            count !=count
    print(count)

