from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        ans = 1
        pre,cur = 0,0
        for i in range(len(nums)-1):
            cur = nums[i+1]-nums[i]
            # 这里=0是为两把第一个计算进来
            if cur*pre<=0 and cur!=0:
                ans+=1
                pre = cur
        return ans