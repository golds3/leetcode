from typing import List


class Solution:
    """
    切割和组合其实是一个道理，组合选择第i+1个，相当于从第i+1开始切割
    """
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def is_s(s:str)->bool:
            if len(s) ==1:
                return True
            left,right = 0,len(s)-1
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        def dfs(start:int,cur:List[str]):
            if start==len(s):
                ans.append(cur)
                return
            for i in range(start,len(s)):
                if not is_s(s[start:i+1]):
                    continue
                dfs(i+1,cur+[s[start:i+1]])

        dfs(0,[])
        return ans



