from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        max_sum = nums[0]
        for num in nums:
            if sum < 0:
                sum = 0
            sum += num
            max_sum = max(sum,max_sum)
        return max_sum

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))