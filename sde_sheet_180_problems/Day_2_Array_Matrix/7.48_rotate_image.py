from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                print(f"matrix: {matrix}")
        for row in matrix:
            print(f"row:{row}")
            for j in range(n//2):
                print(row[j],row[~j])
                row[j], row[~j] = row[~j], row[j]

s= Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(f"Given matrix: {matrix}")
s.rotate(matrix)
print(matrix)