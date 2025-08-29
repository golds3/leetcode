class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp(i,j) 表示：在网格中，以 (i,j) 为右下角、且全为 '1' 的最大正方形的边长。
        dp = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        max_len = 0
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                if matrix[i - 1][j - 1] == "0":
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    max_len = max(max_len, dp[i][j])
        return max_len * max_len
