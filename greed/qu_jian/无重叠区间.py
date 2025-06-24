from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort(key=lambda x:x[1])
        for i in range(1,len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                ans += 1
                intervals[i][1] = intervals[i-1][1]
        return ans


