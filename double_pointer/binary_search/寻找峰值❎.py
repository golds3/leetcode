from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        二分的思想，如果num[i] < nums[i+1] ,那么向右走
        如果 nums[i-1]>nums[i],那么向左走
        """
        if len(nums) == 1:
            return 0

        def get_value(i):
            if i < 0 or i >= len(nums):
                return float("-inf")
            return nums[i]

        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if get_value(mid - 1) < get_value(mid) > get_value(mid + 1):
                return mid
            elif get_value(mid) <= get_value(mid + 1):
                left = mid + 1
            else:
                right = mid
        return -1
