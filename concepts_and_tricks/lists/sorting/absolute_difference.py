# Problem
"""
You are given n numbers, 
find the smallest difference between any two numbers

Example: [8,1,5,12]
output: 3
"""

# Naive solution

def naive_solution(arr):
    """
        Loop through the arr and compare each element to find the 
        smallest difference and finally return the smallest
    """
    min_value = float("inf")
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
           diff =  abs(arr[i]- arr[j])
           if min_value>diff:
               min_value = diff

    return min_value
# print(naive_solution([8,1,5,12]))

# Optmized solution O(nlogn)
def optmized_solution(arr):
    """
    If strings are sorted, then the min difference will be obtained 
    between adjacent numbers
    """
    arr.sort()
    ans = float("inf")
    for i in range(len(arr)-1):
        diff = arr[i+1]-arr[i]
        ans = min(ans,diff)
    return ans
print(optmized_solution([8,1,5,12]))