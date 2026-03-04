#  2 7 5 =  2 + 7 // 2 = 4 + 5 // 2 == 4
# 2/2== 1 + 3// 2 = 1 == 1 
# 1 -1 -4 5 1 -4 = 0 + -2 + 5 / 2 2 + - 4 

#  2 + 7 + 5 = 14// 3 = 4



t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split(" ")))

    target = int(input())
    # total = sum(a)
    # if total//n == target:
    #     print("Yes")
    # else:
    #     print("NO")
    for _ in range(n):
        while len(a)<=1:
            tatal = a.pop(0) + a.pop(1)
            current = tatal//2
            a.insert(0,current)
        print(a)
        if a[0]== target:
            print("yes")
        else:
            print("no")
    
