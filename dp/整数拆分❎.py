class Solution:
    def integerBreak(self, n: int) -> int:
        # dp[i] 和为i 的最大乘积
        # dp[i] = max(dp[i-k] *k)
        if n <=2:
            return n
        dp = [0]*(n+1)
        dp[1] = 1
        for i in range(1,n+1):
            for j in range(1,i):
                dp[i] = max(dp[i], j*dp[i-j],(i-j)*j)
        return dp[-1]


if __name__=='__main__':
    s = Solution()
    print(s.integerBreak(10))

