class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)-1, -1, -1):
            for j in range(i,len(s)):
                if s[i] == s[j] and (j-i<=1 or dp[i+1][j-1]):
                    dp[i][j] = True
                    ans += 1
        return ans




if __name__ == '__main__':
    s = Solution()
    print(s.countSubstrings("abc"))