from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        s = sum(stones)
        target =s//2
        dp = [0]*(target+1)
        for n in stones:
            for j in range(target,n-1,-1):
                dp[j] = max(dp[j],dp[j-n]+n)
        return s-2*dp[target]