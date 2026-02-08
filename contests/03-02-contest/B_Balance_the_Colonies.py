# its frequency problem, thats ceiling techniquel
# 12 and need n groupts 
# n = n - (d-1)/d , and d = colonies 
#   = 12 - (1)/2
import math
# 2 = n - d-1/d
# 2d = n- d-1
# 3d = n-1
# d = n+1/3

# d= 11/3
# print(6//3)

# groups = n+1/3
# but n of people
# it actually the reminder after deving in groups

# n = 5-1/2
# n = 1//2 = 1
#  = n%2 
#  = 

# print(1%2)

# solution
t = int(input())
for _ in range(t):
    n = int(input())
    groups = (n+1)//3
    # print(groups)
    if groups == 1:
        print(n)
    else:
        people = (n-(groups-1))//groups
        print(n-people)



