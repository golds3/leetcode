from typing import List


class Solution:
    """
    给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

    示例 1：



    输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
    输出：6
    解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
    示例 2：

    输入：height = [4,2,0,3,2,5]
    输出：9
    """
    def trap(self, height: List[int]) -> int:
        #有凹处的地方才能装雨水----找下一个更大的元素--->单调递减栈  a>b<c  b -- 凹处 ，面积由a，c决定
        '''
        单调栈是按照 行 的方向来计算雨水
        从栈顶到栈底的顺序：从小到大
        通过三个元素来接水：栈顶，栈顶的下一个元素，以及即将入栈的元素
        雨水高度是 min(凹槽左边高度, 凹槽右边高度) - 凹槽底部高度
        雨水的宽度是 凹槽右边的下标 - 凹槽左边的下标 - 1（因为只求中间宽度）
        '''
        ans = 0
        stack = []
        for k,v in enumerate(height):
            while stack and height[stack[-1]] < v:
                index = stack.pop()
                #左边的柱子
                if stack:
                    h = min(height[stack[-1]],v) - height[index]
                    w = k-stack[-1]-1
                    ans += h*w
            stack.append(k)
        return ans

if __name__ == '__main__':
    s = Solution()
    s.trap([4,2,0,3,2,5])
    assert s.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert s.trap([4,2,0,3,2,5]) == 9








