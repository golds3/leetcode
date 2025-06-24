class Solution:
    def fn(self,n:int)->int:
        # 排列+完全背包
        dp = [0]*(n+1)
        dp[0] = 1
        for j in range(n+1):
            for i in range(1,m+1):
                if j>=i:
                    dp[j] += dp[j-i]
        return dp[n]


if __name__ == '__main__':
    n,m = map(int,input().split())
    print(Solution().fn(n))
