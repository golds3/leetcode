from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: x[0])  # 左边界排序
        print(intervals)
        left = intervals[0][0]
        ans = []
        for i in range(1, len(intervals)):
            if intervals[i][0] <= intervals[i - 1][1]:
                intervals[i][1] = max(intervals[i][1], intervals[i - 1][1])
            else:
                ans.append([left, intervals[i - 1][1]])
                left = intervals[i][0]
            if i == len(intervals) - 1:
                ans.append([left, intervals[i][1]])
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))
