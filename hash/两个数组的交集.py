from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = {}
        ans = set()
        for v in nums1:
            m[v] = True
        for v in nums2:
            if v in m:
                ans.add(v)
        return list(ans)

