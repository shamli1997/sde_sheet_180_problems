# Make first row and first column to mark which row and column should be zero before filling them out,
# then fill the matrix from right to left, and make the first row zero in the last if first row has any zero.
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        firstRowHasZero = not all(matrix[0])
        # set 0 to the first dummy col and row
        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        # traverse backwards and make ele 0 if the ele in dummy row/col is 0
        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])-1,-1,-1):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        # if first row has 0 then make all the elements in that row 0
        if firstRowHasZero:
            matrix[0] = [0]*len(matrix[0])


s = Solution()
matrix = [[0,1,1],[1,0,1],[1,1,1]]
s.setZeroes(matrix)
print(matrix)