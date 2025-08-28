from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def binar_search(target):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        l = binar_search(target)
        if l < 0 or l >= len(nums) or nums[l] != target:
            return [-1, -1]
        r = binar_search(target + 1) - 1
        return [l, r]
