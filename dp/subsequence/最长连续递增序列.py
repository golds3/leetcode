from typing import List


class Solution:
    # 子数组
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 1
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
                ans = max(ans, dp[i])
        return ans
