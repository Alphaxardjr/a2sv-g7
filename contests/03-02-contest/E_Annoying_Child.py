t = int(input())
from collections import Counter
for _ in range(t):
    l = int(input())
    coins = list(map(int,input().split(" ")))
    # odds = [x for x in coins if x%2!=0]
    # evens = [x for x in coins if x%2==0]
    # coins = odds.sort(reverse=True) + evens
    purse = Counter(coins)
    # coins.sort(reverse=True)
    total = 0
    for i in range(l):
        pick =max(coins)
        visted = []
        total +=pick
        if total %2 == 0:
            total = 0
        print(total,end=" ")
    print()  
