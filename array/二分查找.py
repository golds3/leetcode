from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left<=right:
            mid = left + ((right - left)>>1)
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
        return -1


if __name__ == '__main__':
    so =Solution()
    print(so.search([-1,0,3,5,9,12],9))