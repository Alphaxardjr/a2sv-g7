def removeSmallest():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        arr = list(map(int, input().split()))
        
        arr.sort()  # Sort the array first
        possible = True
        
        for i in range(n - 1):
            if arr[i+1] - arr[i] > 1:
                possible = False
                break
        
        print("YES" if possible else "NO")

removeSmallest()