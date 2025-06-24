from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] 选nums[i]作为结尾的最长子序列 ！！！
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS([1,1,1,1,1]))

