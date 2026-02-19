# t = int(input())
# from collections import Counter
# for _ in range(t):
#     l = int(input())
#     coins = list(map(int,input().split(" ")))
#     # odds = [x for x in coins if x%2!=0]
#     # evens = [x for x in coins if x%2==0]
#     # coins = odds.sort(reverse=True) + evens
#     purse = Counter(coins)
#     # coins.sort(reverse=True)
#     total = 0
#     for i in range(l):
#         pick =max(coins)
#         visted = []
#         total +=pick
#         if total %2 == 0:
#             total = 0
#         print(total,end=" ")
#     print()  

test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    nums = list(map(int, input().split()))
    odds = []
    evens = []
    for i in range(n):
        if nums[i] % 2:
            odds.append(nums[i])
        else:
            evens.append(nums[i])
    ans = [0] * n
    if not odds:
        print(*ans)
        continue
    evens.sort(reverse=True)
    e = len(evens)
    o = len(odds)
    pre = [0] * (e+1)
    for i in range(e):
        pre[i+1] = pre[i] + evens[i]
    
    odd_maxx = max(odds)
    for k in range(1,n+1):
        # odd_count + even_count = k    [minn, maxx]     choice A: 1 odd + (k-1) evens 
        minn = max(1, k-e)                               #choice B: 3odd + (k-3) odd                 
        maxx = min(k,o)
        odd_coins = minn if minn % 2 else minn + 1

        if odd_coins > maxx:
            ans[k-1] = 0
        else:
            even_coins = k - odd_coins
            ans[k-1] = odd_maxx + pre[even_coins]
    print(*ans)
