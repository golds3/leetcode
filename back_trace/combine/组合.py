from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        tmp = []
        ans = []
        def dfs(start):
            nonlocal ans
            nonlocal tmp
            if len(tmp) == k:
                ans.append(tmp.copy())
                return
            # 剪枝，如果后序的个数已经不足凑成k个，就不用去遍历了
            for i in range(start, n+1-(k-len(tmp))+1):
                tmp.append(i)
                dfs(i+1)
                tmp.pop()
        dfs(1)
        return ans




