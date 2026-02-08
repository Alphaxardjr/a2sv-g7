# n = a + b
# a>b

# n_ways = n - 1//2 - universal seiling method 
# 7+1//2 == 8/2

# 1-1/2 = 0 
# print((2000000000-1)//2)

n = int(input())
for _ in range(n):
    biscuit = int(input())
    print((biscuit-1)//2)
