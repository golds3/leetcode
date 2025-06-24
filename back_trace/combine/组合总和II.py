from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def dfs(start:int,cur:list[int]):
            if sum(cur) == target:
                ans.append(cur)
                return
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                if sum(cur)+candidates[i]>target:
                    break
                dfs(i+1,cur+[candidates[i]])
        dfs(0,[])
        return ans

