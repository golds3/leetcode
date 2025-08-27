class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        col = [False for _ in range(n)]
        diag1 = [False] * (2 * n - 1)  # row - col 取值范围 [-n+1, n-1]，偏移 n-1
        diag2 = [False] * (2 * n - 1)  # row + col 取值范围 [0, 2n-2]

        def dfs(i, queen):
            nonlocal ans
            if queen == n:
                ans += 1
                return
            if i >= n:
                return
            for j in range(n):
                if not col[j] and not diag1[i - j + n - 1] and not diag2[i + j]:
                    col[j] = diag1[i - j + n - 1] = diag2[i + j] = True
                    dfs(i + 1, queen + 1)
                    col[j] = diag1[i - j + n - 1] = diag2[i + j] = False

        dfs(0, 0)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.totalNQueens(4))
