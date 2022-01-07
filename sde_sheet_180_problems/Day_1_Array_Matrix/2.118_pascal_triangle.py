from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]*(i+1) for i in range(numRows)]
        print(f"pascal: {pascal}")
        for i in range(numRows):
            for j in range(1,i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
                print(f"i:{i} j:{j} pascal[{i}][{j}] : {pascal[i][j]}")
        return pascal

s = Solution()
print(s.generate(5))