from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(start:int,cur:list[int]):
            if sum(cur) > target:
                return
            if sum(cur)==target:
                ans.append(cur)
                return
            for i in range(start,len(candidates)):
                dfs(i,cur+[candidates[i]])
        dfs(0,[])
        return ans


if __name__ == '__main__':
    s  = Solution()
    print(s.combinationSum([2,3,6,7],7))