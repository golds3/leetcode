from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        for v in coins:
            for j in range(v,amount+1):
                dp[j] +=dp[j-v]
        return dp[-1]