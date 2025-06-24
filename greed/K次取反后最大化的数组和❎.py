from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort(key=lambda x:abs(x),reverse=True) # 按照绝对值从大到小
        for i in range(len(nums)):
            if k > 0 and nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
        if k > 0 and k % 2 != 0:
            nums[-1] = -nums[-1]
        return sum(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.largestSumAfterKNegations([-8,3,-5,-3,-5,-2], 6))
