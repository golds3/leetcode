from typing import List


class Solution:
    """
    给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

    求在该柱状图中，能够勾勒出来的矩形的最大面积。
    输入：heights = [2,1,5,6,2,3]
    输出：10
    解释：最大的矩形为图中红色区域，面积为 10

    输入： heights = [2,4]
    输出： 4
    """
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 矩形的最大面积。 --- 下一个最小 -- 单调递减
        ans = 0
        stack = []
        heights.append(0) #应对单调递增的情况
        heights.insert(0,0) # 最左边插入，用于计算第一个柱子的面积--- 计算面积需要用到前一个柱子的下标
        for k,v in enumerate(heights):
            while stack and heights[stack[-1]] > v:
                index = stack.pop()
                if stack:
                    ans = max(ans, heights[index] * (k-stack[-1]-1))
            stack.append(k)
        return ans

    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     heights.insert(0, 0)
    #     heights.append(0)
    #     stack = [0]
    #     result = 0
    #     for i in range(1, len(heights)):
    #         while stack and heights[i] < heights[stack[-1]]:
    #             mid_height = heights[stack[-1]]
    #             stack.pop()
    #             if stack:
    #                 # area = width * height
    #                 area = (i - stack[-1] - 1) * mid_height
    #                 result = max(area, result)
    #         stack.append(i)
    #     return result


if __name__ == '__main__':
    s = Solution()
    assert s.largestRectangleArea([2,1,5,6,2,3]) == 10
    assert s.largestRectangleArea([2,1,2]) == 3