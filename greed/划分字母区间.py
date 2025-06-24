from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        start, end = 0, 0
        # 最后出现的位置，就是切割点
        hash = {}
        for k, v in enumerate(s):
            hash[v] = k
        for i in range(len(s)):
            end = max(end, hash.get(s[i]))
            if i == end:
                ans.append(i - start + 1)
                start = i + 1
        return ans

