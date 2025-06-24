from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[0, 0] for _ in range(k)]
        for i in range(k):
            dp[i][0] = -prices[0]
        for i in range(1, len(prices)):
            for j in range(k):
                if j > 0:
                    dp[j][0] = max(dp[j][0], dp[j - 1][1] - prices[i])
                    dp[j][1] = max(dp[j][1], dp[j][0] + prices[i])
                else:
                    dp[j][0] = max(dp[j][0], -prices[i])
                    dp[j][1] = max(dp[j][1], dp[j][0] + prices[i])
        return dp[-1][1]


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit(2, [2,4,1]))
