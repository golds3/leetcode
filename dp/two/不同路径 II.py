from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # dp[i][j] 到达 i,j的路径数
        # dp[i][j] = dp[i-1][j]+dp[i][j-1]
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp = [[0]*n]*m
        for i in range(m):
            if obstacleGrid[i][0]==1:
                break
            dp[i][0]=1
        for j in range(n):
            if obstacleGrid[0][j]==1:
                break
            dp[0][j]=1
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==1:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        for i in range(m):
            print(dp[i])
        return dp[-1][-1]

if __name__ == '__main__':
    s = Solution()
    s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
