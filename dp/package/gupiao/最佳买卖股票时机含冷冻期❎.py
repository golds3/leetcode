from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 0 -持有 1-之前就不持有，2-今天不持有 3- 冷冻期
        dp = [0]*4
        dp[0] = -prices[0]
        for i in range(1,len(prices)):
            tmp = dp.copy()
            dp[0] = max(tmp[0],tmp[1]-prices[i],tmp[3]-prices[i])
            dp[1] = max(tmp[1],tmp[3])
            dp[2] = tmp[0]+prices[i]
            dp[3] = tmp[2]
        return max(dp)
