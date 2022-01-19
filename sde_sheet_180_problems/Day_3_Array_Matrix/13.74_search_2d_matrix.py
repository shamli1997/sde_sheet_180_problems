from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        if not len(matrix): return False
        hi = (len(matrix) * len(matrix[0])) - 1
        
        while lo <= hi:
            mid = (lo + (hi - lo) // 2)
            if matrix[mid//len(matrix[0])][mid % len(matrix[0])] == target: return True
            if matrix[mid//len(matrix[0])][mid % len(matrix[0])] < target: lo = mid + 1
            else:hi = mid - 1
        return False

s = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 10
print(s.searchMatrix(matrix,target))