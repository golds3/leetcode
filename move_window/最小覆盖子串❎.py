from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        cnt = Counter(t)
        less = len(cnt)
        left,right = -1,len(s)
        index = 0
        for k,v in enumerate(s):
            cnt[v]-=1
            if cnt[v]==0:
                less-=1
            while less==0:
                if right-left>k-index:
                    left,right = index,k
                if cnt[s[index]]==0:
                    less+=1
                cnt[s[index]]+=1
                index+=1
        return "" if right==len(s) else s[left:right+1]            

