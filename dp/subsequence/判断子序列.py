class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m,n = len(s), len(t)
        if m>n:
            return False
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    # 不匹配，因为是要匹配s，所以只删除t的字母就行了
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1] == m

