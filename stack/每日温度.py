from typing import List


class Solution:
    """
    给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。

    示例 1:

    输入: temperatures = [73,74,75,71,69,72,76,73]
    输出: [1,1,4,2,1,1,0,0]
    示例 2:

    输入: temperatures = [30,40,50,60]
    输出: [1,1,1,0]
    示例 3:

    输入: temperatures = [30,60,90]
    输出: [1,1,0]
    """

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 求下一个更高温度，维护一个单调递减栈
        statck = []
        ans = [0]*len(temperatures)
        for k,temp in enumerate(temperatures):
            while statck and temperatures[statck[-1]]<temp:
                index = statck.pop()
                ans[index] = k-index
            statck.append(k)
        return ans




if __name__ == "__main__":
    so = Solution()
    # print(so.dailyTemperatures([73,74,75,71,69,72,76,73]))
    assert so.dailyTemperatures([73,74,75,71,69,72,76,73])==[1,1,4,2,1,1,0,0]
    assert so.dailyTemperatures([30,40,50,60])==[1,1,1,0]
    assert so.dailyTemperatures([30,60,90])==[1,1,0]

