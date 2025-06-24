from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 快慢指针
        slow,fast =0,0
        ans = 0
        while fast<len(nums):
            if nums[fast]!=val:
                nums[slow],nums[fast]=nums[fast],nums[slow]
                slow+=1
                ans+=1
            fast+=1
        return ans
    # 左右指针
    def removeElement(self, nums: List[int], val: int) -> int:
        # 快慢指针
        ans = 0
        left,right = 0,len(nums)-1
        while left<=right:
            if nums[left]==val:
                nums[left],nums[right]=nums[right],nums[left]
                right-=1
                continue
            ans+=1
            left+=1
        return ans
