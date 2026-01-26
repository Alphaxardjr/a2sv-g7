n = int(input())

for i in range(n):
    initial = 5
    remaining = 0
    output = 0
    a,b,c= map(int,input().split(" "))
    if a<initial:
        remaining = initial-a
        a = 5

        if remaining !=0 and b<5:
            b = b+remaining
            remaining

        output = a*b*c
        print(output)
    else:
        remaining = initial
        b= b+remaining
        output = a*b*c

