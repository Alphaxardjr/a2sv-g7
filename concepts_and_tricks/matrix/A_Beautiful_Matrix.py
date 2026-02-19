matrix = []
for _ in range(5):
    row= list(map(int,input().split(" ")))
    matrix.append(row)
c_row,c_col = 2,2
for row in range(5):
    for col in range(5):
        if matrix[row][col]==1:
            pos_row,pos_col = row,col
            steps = abs(pos_row-2) + abs(pos_col-2) 
            print(steps)
            break