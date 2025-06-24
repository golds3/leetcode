from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float("-inf")
        tmp = 0
        for i in range(len(nums)):
            if tmp < 0:
                tmp = nums[i]
            else:
                tmp += nums[i]
            ans = max(ans, tmp)
        return ans


