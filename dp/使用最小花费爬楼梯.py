from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[i] 到达第i层第最小花费
        # dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        dp = [0]*(1+len(cost))
        for i in range(2,len(cost)+1):
            dp[i]  = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minCostClimbingStairs([10,15,20]))