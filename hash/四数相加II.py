from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        m = dict()
        ans = 0
        for a in nums1:
            for b in nums2:
                m[a+b] = m.get(a+b,0)+1
        for c in nums3:
            for d in nums4:
                if -c-d in m:
                    ans+=m[-c-d]
        return ans

if __name__ == '__main__':
    so = Solution()
    print(so.fourSumCount([-1,-1],[-1,1],[-1,1],[1,-1]))