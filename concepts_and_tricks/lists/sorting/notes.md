## Sorting

simple ascending sorting, it returns new sorted list
new_sorted = sorted([5, 2, 3, 1, 4])

list.sort() method modified the list in place
a = [5, 2, 3, 1, 4]
a.sort() It returns None and modifies the list in place

key functions

sort functions have a key parameter that takes in a functionr or other collable  and its called once for each input record

example:
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])   # sort by age

## Frequency Counting
 Used when the problem asks?

 - how many times
 - most frequent
 - duplicates
 - pairs with same values

## Prefix sum
  Used when
  - many sum queries
  - subarray sum
  - ranges
  The trick
  - Precompute once to get O(1)
  
