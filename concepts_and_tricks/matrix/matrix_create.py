matrix =[
    [1,2,3,4,5,],
    [6,7,8,9,10],
    [11,12,13,14,15]
]


# traverse the matrix

result = 0
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        result+=matrix[row][col]
# print(result)
row = 0
col = 1

for dr in [-1,0,1]:
    for dc in [-1,0,1]:
        print(dr+row,dc+col)
        print("--")
