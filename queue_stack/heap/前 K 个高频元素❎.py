import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        # 最小二叉堆
        map = {}  # nums[i]:对应出现的次数
        for i in range(len(nums)):
            map[nums[i]] = map.get(nums[i], 0) + 1
        for v in map:
            # heappush 对于tuple 按照第一位进行排序
            heapq.heappush(min_heap, (map[v],v))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(min_heap)[1])
        return ans


if __name__ == '__main__':
    so = Solution()
    print(so.topKFrequent([1,1,1,2,2,3], 2))
