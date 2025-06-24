from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #放到后面就行
        left,right = 0 ,len(nums)-1
        while left<=right:
            if nums[left] == val:
                nums[left],nums[right] = nums[right],nums[left]
                right-=1
            else:
                left+=1
        return left
    def removeElement2(self, nums: List[int], val: int) -> int:
        #放到后面就行
        slow,fast = 0,0
        while fast<len(nums):
            if nums[fast]!=val:
                nums[slow] = nums[fast]
                slow+=1
            fast+=1
        return slow

if __name__ == '__main__':
    so = Solution()
    print(so.removeElement([1],1))