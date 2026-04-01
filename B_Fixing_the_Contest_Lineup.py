t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    counter = 0
    i = 0
    while i<len(b):
        if b[i]< a[i]:
            a.pop()
            a.append(b[i])
            a.sort()
            counter +=1
        i +=1
    print(counter)
       