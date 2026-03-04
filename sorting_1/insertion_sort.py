arr = [ 3,7,9,11,12 ]
n = len(arr)

for i in range(1,n):
    key = arr[i]
    j= i-1
    while j>=0 and key <arr[j]:
        arr[j+1]= arr[j]
        j -=1
    arr[j+1]= key
print(arr)