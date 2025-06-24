from typing import List


class Solution:
    #暴力解法是O(n^3),使用双指针进行二分查找优化为O(n^2)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #因为答案不要求顺序，我们假设三元祖a,b,c的关系是 a<b<c
        nums.sort()
        ans = []
        for k,v in enumerate(nums):
            if v>0:
                break
            if k>0 and v==nums[k-1]:
                continue
            p1,p2 = k+1,len(nums)-1
            while p1<p2:
                if nums[p1]+nums[p2]+v<0:
                    p1+=1
                elif nums[p1]+nums[p2]+v>0:
                    p2-=1
                else:
                    ans.append([v,nums[p1],nums[p2]])
                    while p1<p2 and nums[p1]==nums[p1+1]:p1+=1
                    while p1<p2 and nums[p2]==nums[p2-1]:p2-=1
                    p1+=1
                    p2-=1

        return ans

if __name__ == '__main__':
    so = Solution()
    print(so.threeSum([-1,0,1,2,-1,-4]))

