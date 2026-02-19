``` python 
    rows,cols = (3,3) # initialization of cols and rows
    mat =[[0]*cols]*rows # matrix definition

    # Initializing a 2-D array with values
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

### Operations on a matrix
1. accessing element in a matrix , mat[row][col]
2. Traversal of a Matrix - uses 2 for loop 
    ``` python
        # Traversing each row
        for row in arr:
        
            # Traversing each element
            # in the current row
            for x in row:
                print(x, end=" ")
            print()
    ```
3. Searching in a Matrix
    ``` python 
        rows, cols = len(arr), len(arr[0])

        # Traverse each row and column
        for i in range(rows):
            for j in range(cols):
                if arr[i][j] == x:
                    return True
        return False
    ```
4. Sorting matrix
    - Row wise sorting a 2D array.
     The idea is to traverse through the rows and call sort method on each row
        ``` python 
            def sortRows(mat):
                for row in mat:
                    row.sort()
        ```
    - Sort the matrix column-wise
      - Steps
      1. Traverse the matrix
      2. Find the transpose of the matrix
      3. Store the transpose of a matrix in 2d array/ vector, tr[][]
      4. traverse the rows of the matrix tr[][]
      5. sort each row of the matrix
      6. store the transpose of tr[][] in mat [][]
      7. return the matrix [][]
    ``` python 
        def sortRows(mat):
            for row in mat:
                row.sort()
    ```

