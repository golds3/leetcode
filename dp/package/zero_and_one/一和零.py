from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for v in strs:
            zero,one = v.count("0"), v.count("1")
            for j in range(m,zero-1,-1):
                for k in range(n,one-1,-1):
                    dp[j][k] = max(dp[j][k],dp[j-zero][k-one]+1)
        return dp[m][n]