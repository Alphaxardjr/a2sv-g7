"""
 Given the list, print the number that appear most
 Example:
    input: [1,2,2,3,3,3]
    output: 3
"""

def naive_solution(arr):
    pass


def optimized_solution(arr):
    frequncy = {}
    most_number = None
    most_count = 0
    for num in arr:
        frequncy[num] = frequncy.get(num,0)+1
        if frequncy[num]>most_count:
            most_count = frequncy[num]
            most_number = num
    return most_number

print(optimized_solution([1,2,2,3,3,3]))