from typing import List
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n= len(img[0])
        m = len(img)
        result = [[0]*n for _ in range(m)]
       
        for row in range(len(img)):
            
            for col in range(len(img[row])):
                total = 0
                count = 0
                for dr in [-1,0,1]:
                    for dc in [-1,0,1]:
                        nr = row + dr
                        nc = col + dc 

                        if 0 <= nr < n and  0<= nc < m:
                            # print("its running")
                            total += img[nr][nc]
                            count +=1

            result[row][col]= total//count
        return result
                
                
    def binaryGrid(self,binary:List[List[int]]) ->List[List[int]]:

        m= len(binary) # rows
        n =len(binary[0]) # colmn
        result = [[0]*n for _ in range(m)]
        for row in range(m):
            for col in range(n):
                total = 0
                for dr in [-1,0,1]:
                    for dc in [-1,0,1]:
                        if dr ==0 and dc == 0:
                            continue
                        nr = row + dr
                        nc = col + dc
                        if 0<=nr<m and 0<= nc <n:
                            if binary[nr][nc]== 1:
                                total +=1
                result[row][col]=total
            
        return result
    def is_symmetric(self,matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):  # only upper triangle
                print(matrix[i][j])
                # if matrix[i][j] != matrix[j][i]:
                #     return False
        return True
    def is_good(self,mat: List[List[int]]) -> List[List[int]]:
        """
        Count “good” cells. A cell is good if it is strictly greater 
        than all 4 neighbors (up, down, left, right).
        """

        m = len(mat)
        n = len(mat[0])
        for row in range(m):
            for col in range(n):
                
        pass
    
binary = [
 [1,0,1],
 [0,1,0],
 [1,0,1]
]

sym1  = [
 [1, 2, 3],
 [2, 5, 6],
 [3, 6, 9]
]

img = [[1,1,1],[1,0,1],[1,1,1]]

sol1 = Solution()
# print(sol1.imageSmoother(img))
# print(sol1.binaryGrid(binary))
sol1.is_symmetric(sym1)

