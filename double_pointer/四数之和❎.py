from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for k,v in enumerate(nums):
            if v>target and v>=0:
                break
            if k>0 and v==nums[k-1]:
                continue
            p1 = k+1
            while p1<len(nums):
                if v+nums[p1]>target and v+nums[p1]>=0:
                    break
                if p1>k+1 and nums[p1]==nums[p1-1]:
                    p1+=1
                    continue
                p2,p3 = p1+1,len(nums)-1
                while p2<p3:
                    if v+nums[p1]+nums[p2]+nums[p3]<target:
                        p2+=1
                    elif v+nums[p1]+nums[p2]+nums[p3]>target:
                        p3-=1
                    else:
                        ans.append([v,nums[p1],nums[p2],nums[p3]])
                        while p2<p3 and nums[p2]==nums[p2+1]:p2+=1
                        while p2<p3 and nums[p3]==nums[p3-1]:p3-=1
                        p2+=1
                        p3-=1
                p1+=1
        return ans


if __name__ == '__main__':
    so = Solution()
    print(so.fourSum([1,0,-1,0,-2,2], 0))