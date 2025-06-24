from collections import deque


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        arr = deque()
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
            arr.appendleft(dp[i])
        for i in arr:
            print(i)
        return dp[0][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindromeSubseq("babad"))




