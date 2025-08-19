from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        tl, tr = newInterval

        def find_left(pos, target, strict=False):
            """
            我们要找的两个边界

            li = 第一个右端点 >= tl

            条件是 “大于等于”

            因为只要右端点覆盖了 tl，就说明它可能和新区间重叠。

            ri = 第一个左端点 > tr

            条件是 “严格大于”

            因为如果左端点 == tr，那其实还是重叠的（题目定义区间是闭区间 [a,b]）。

            例子：新区间 [1,5]，原区间 [5,7]，它们 确实重叠，应该合并。

            如果你用 >=，会把 [5,7] 错误地归到右边，不合并。

            所以 strict 的意义

            strict=False → 用 >= target
            👉 找 “第一个 ≥ target 的位置”
            👉 适合用在 li（右端点 ≥ newInterval.left）

            strict=True → 用 > target
            👉 找 “第一个 > target 的位置”
            👉 适合用在 ri（左端点 > newInterval.right）
            """
            left, right = 0, len(intervals) - 1
            ans = len(intervals)
            while left <= right:
                mid = (left + right) // 2
                if (intervals[mid][pos] > target) or (
                    not strict and intervals[mid][pos] >= target
                ):
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return ans

        # 找到第一个右端点 >= tl 的
        li = find_left(1, tl)
        # 找到第一个左端点 > tr 的
        ri = find_left(0, tr, strict=True)

        if li < ri:  # 存在重叠区间
            tl = min(tl, intervals[li][0])
            tr = max(tr, intervals[ri - 1][1])
        return intervals[:li] + [[tl, tr]] + intervals[ri:]


if __name__ == "__main__":
    s = Solution()
    s.insert([[1, 3], [4, 5], [6, 9]], [2, 5])
