from typing import List


class Solution:
    """todo
    其他解法，不用排序的方案
    """
    def hIndex(self, citations: List[int]) -> int:
        """
        要求有n篇论文，每篇论文被引用的个数都>=n
        求n的最大值
        :param citations:
        :return:
        """
        # 0 1 3 5 6
        #
        # 对于 i ，v = nums[i] 如果剩下的文章数量>=v ，那么h = v
        #                     如果剩下的文章数量<v , 那么h = 剩下的文章

        citations.sort()
        h = 0
        length = len(citations)
        for k,v in enumerate(citations):
            if length-k>=v:
                h = max(h,v)
            else:
                h = max(h,length-k)
        return h


if __name__ == '__main__':
    s = Solution()
    print(s.hIndex([3,0,6,1,5]))
    print(s.hIndex([1,3,1]))
    print(s.hIndex([100]))
    print(s.hIndex([11,15]))

