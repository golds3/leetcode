from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        tmp = []
        ans = []
        def dfs(start):
            nonlocal ans
            nonlocal tmp
            if sum(tmp) == n and len(tmp)==k:
                ans.append(tmp.copy())
                return
            # 根据sum剪枝
            if sum(tmp) >n:
                return
            # 根据k剪枝
            for i in range(start,10-(k-len(tmp))+1):
                tmp.append(i)
                dfs(i+1)
                tmp.pop()
        dfs(1)
        return ans