from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(index):
            if index == len(nums):
                ans.append(nums.copy())
                return
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                dfs(index + 1)
                nums[index], nums[i] = nums[i], nums[index]

        dfs(0)
        return ans
