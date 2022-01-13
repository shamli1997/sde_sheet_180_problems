from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prev = intervals[0]
        result = [prev]

        for i in intervals[1:]:
            if i[1] <= prev[1]:
                continue
            # if i and prev overlap, e.g., [1,3] and [2,6], change i[0] = prev[0] and pop out prev
            elif i[0] < prev[1]:
                i[0]=prev[0]
                result.pop()
            result.append(i)
            prev = i
        return result

s = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(s.merge(intervals))
