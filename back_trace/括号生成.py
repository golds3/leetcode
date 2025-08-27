from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(left, right, tmp):
            if len(tmp) == 2 * n:
                ans.append(tmp)
                return
            # 优先左括号
            for i in range(left, n):
                dfs(i + 1, right, tmp + "(")
            if left > right:
                for i in range(right, n):
                    dfs(left, i + 1, tmp + ")")

        dfs(0, 0, "")
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))
