class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True

        # 初始化第一列
        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        # 初始化第一行
        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        # 状态转移
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                    dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                )

        return dp[-1][-1]

    def isInterleave_v2(self, s1: str, s2: str, s3: str) -> bool:
        """
        滚动数组优化
        """
        if len(s3) != len(s1) + len(s2):
            return False

        dp = [False] * (len(s2) + 1)
        dp[0] = True
        for i in range(1, len(s2) + 1):
            dp[i] = dp[i - 1] and s2[i - 1] == s3[i - 1]
        # 状态转移
        for i in range(1, len(s1) + 1):
            # 更新第一列
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, len(s2) + 1):
                dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (
                    dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                )

        return dp[-1]
