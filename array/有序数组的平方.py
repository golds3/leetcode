from typing import List

"""注意，nums已经的有序的了"""
class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x:abs(x))
        return [x*x for x in nums]


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, i = 0, len(nums)-1, len(nums)-1
        res = [float('inf')] * len(nums) # 需要提前定义列表，存放结果
        while l <= r:
            if nums[l] ** 2 < nums[r] ** 2: # 左右边界进行对比，找出最大值
                res[i] = nums[r] ** 2
                r -= 1 # 右指针往左移动
            else:
                res[i] = nums[l] ** 2
                l += 1 # 左指针往右移动
            i -= 1 # 存放结果的指针需要往前平移一位
        return res

if __name__ == '__main__':
    so = Solution()
    print(so.sortedSquares([-4,-1,10,3,0]))