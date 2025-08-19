from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # 模拟,快慢指针
        ans = []
        start, end = 0, 0
        while end < len(nums):
            while end < len(nums) - 1 and nums[end + 1] == nums[end] + 1:
                end += 1
            if nums[end] == nums[start]:
                ans.append(str(nums[start]))
            else:
                ans.append(str(nums[start]) + "->" + str(nums[end]))
            end += 1
            start = end
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.summaryRanges([0, 2, 3, 4, 6, 8, 9]))
