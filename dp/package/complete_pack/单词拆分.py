from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for v in wordDict:
                if i>=len(v):
                    dp[i] = dp[i-len(v)] and s[i-len(v):i] == v
                    if dp[i]:
                        break
        return dp[-1]
