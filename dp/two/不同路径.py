class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j] 到达 i,j的路径数
        # dp[i][j] = dp[i-1][j]+dp[i][j-1]
        dp = [[0]*n]*m
        dp[0] = [1]*n
        for i in range(1, m):
            dp[i][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]