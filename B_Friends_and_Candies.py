# [4,5,2,5] - [2,4] == 16/4 == 4
# 0 4 == -[1] === 4/2 == 2 
# 10 8 5 1 4 - -1 ( no way ) == 28/5 = 5  how ? 

# 10000 - 0 - one element 
# 1 1 1 1 1 1 1 - 0 - equal - 7/7 == 1 

t = int(input())

for _ in range(t):
    n = int(input())
    friends = list(map(int,input().split()))

    if sum(friends)%n !=0 :
        print(-1)
    else:
        avarage = sum(friends)//n
        result = [f for f in friends if f > avarage]
        print(len(result))
    # if n == 1 or sum(friends)//n ==1:
    #     print(0)
    # elif sum(friends)%n !=0 :
    #     print(-1)
    # else:
    #     avarage = sum(friends)//n
    #     result = [f for f in friends if f > avarage]
    #     print(result)
