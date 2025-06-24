class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m = {}
        for v in s:
            m[v] = m.get(v, 0) + 1
        for v in t:
            if v not in m:
                return False
            m[v] = m.get(v) - 1
        for _, v in m.items():
            if v!=0:
                return False
        return True


if __name__ == '__main__':
    so = Solution()
    print(so.isAnagram("anagram", "nagaram"))