from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1
        for j in range(target+1):
            for v in nums:
                if j >= v:
                    dp[j] += dp[j-v]
        return dp[-1]
