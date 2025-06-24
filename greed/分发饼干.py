from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child = 0
        for i in range(len(s)):
            if child<len(g) and s[i]>=g[child]:
                child+=1
        return child

if __name__ == '__main__':
    s = Solution()
    print(s.findContentChildren(g=[10, 9, 8, 7], s=[5, 6, 7, 8]))
