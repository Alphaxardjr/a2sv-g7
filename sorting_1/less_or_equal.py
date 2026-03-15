def less_or_equal():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    
    if k == 0:
     
        x = arr[0] - 1
        if x >= 1:
            print(x)
        else:
            print(-1)
    else:
        x = arr[k-1]
        
        if k < n and arr[k] == x:
            print(-1)
        else:
            print(x)
less_or_equal()