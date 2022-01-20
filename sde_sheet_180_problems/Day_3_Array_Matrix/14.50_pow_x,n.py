class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0
        nn = n
        # if nn is negative make it positive
        if nn < 0: nn = -1 * nn
        while nn > 0:
            # if nn is odd power multiply ans with x and dec nn
            if nn %  2 == 1:
                ans = ans * x
                nn = nn - 1
            else:
                # if nn is even then multiply x by itself and divide nn by 2
                x = x * x
                nn = nn // 2
            #   if n is negative then ans is 1/ans
        if n < 0: ans = 1.0 / ans
        return ans
        
s = Solution()
print(s.myPow(2.00000,-2))