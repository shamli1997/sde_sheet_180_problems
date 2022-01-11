from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            min_price = min(min_price,price)
            max_profit = max(max_profit,price - min_price)
        return max_profit

s = Solution()
print(s.maxProfit([1,2,3,4,5,1,11]))