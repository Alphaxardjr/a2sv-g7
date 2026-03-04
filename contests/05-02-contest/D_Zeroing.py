n,k = map(int,input().split(" "))
a = list(map(int,input().split(" ")))

def find_min(a):
    min = a[0]
    for i in a:
        if i !=0 and i<min:
            min = i
            return min

for _ in range(k):
    el = find_min(a)
    if el>0:
        print(el)
        a.insert(a.index(el),0)
    elif sum(a) ==0:
        print(0)