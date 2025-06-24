from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        pre, ml = 0, 0
        for i in range(len(nums)-1):
            ml = max(ml, nums[i]+i)
            if i==pre:
                ans += 1
                pre = ml
        return ans
