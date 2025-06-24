from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 队列中只存储有可能是最大值的元素(单调递减队列)
        queue = deque([nums[0]])
        for i in range(1, k):
            while queue and queue[-1]<nums[i]:
                queue.pop()
            queue.append(nums[i])
        ans = [queue[0]]
        for i in range(k, len(nums)):
            while queue and queue[-1]<nums[i]:
                queue.pop()
            queue.append(nums[i])
            if nums[i-k]==queue[0]:
                queue.popleft()
            ans.append(queue[0])
        return ans



if __name__ == '__main__':
    so = Solution()
    print(so.maxSlidingWindow([-7,-8,7,5,7,1,6,0], 4))
