class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = set(nums)
        ans = 0
        for v in m:
            if v-1 in m:
                continue
            nx = v+1
            while nx in m:
                nx+=1
            ans = max(ans,nx-v)
            if ans>len(nums)//2:break
        return ans            
