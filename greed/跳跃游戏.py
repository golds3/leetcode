from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0
        i = 0
        while i <= cover:
            if cover>=len(nums)-1:
                return True
            cover = max(cover,i+nums[i])
            i += 1
        return False
            
