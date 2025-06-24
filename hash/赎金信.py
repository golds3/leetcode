from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)>len(magazine):
            return False
        m = defaultdict(int)
        for v in magazine:
            m[v] += 1
        for v in ransomNote:
            if m[v]<=0:
                return False
            m[v] -= 1
        return True
