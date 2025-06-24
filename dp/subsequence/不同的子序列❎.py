class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # 编辑 s
        m,n = len(s), len(t)
        if n>m:
            return 0
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 1
        # dp [i][j] 把 s[:i] 编辑成 t[:j] 的方案
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1] == t[j-1]:
                    # 当前匹配，那么可以是同时去掉当前，或者去掉s[i-1]
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    # 不匹配，只能去掉s[i-1]
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]


