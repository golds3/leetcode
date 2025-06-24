from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        left = 0
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            while cur_sum >= target:
                ans = min(ans, i - left + 1)
                cur_sum-=nums[left]
                left += 1
        return ans if ans != float('inf') else 0