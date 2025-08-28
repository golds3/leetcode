from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        找极小值
        """
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums)

        def get_value(i):
            if i < 0 or i >= len(nums):
                return float("inf")
            return nums[i]

        while left < right:
            mid = left + (right - left) // 2
            if get_value(mid - 1) > get_value(mid) < get_value(mid + 1):
                return get_value(mid)
            elif get_value(mid) < get_value(mid + 1):
                right = mid
            else:
                left = mid + 1
        return -1


if __name__ == "__main__":
    s = Solution()
    s.findMin([3, 4, 5, 1, 2])
