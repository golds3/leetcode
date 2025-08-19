class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(s) != len(pattern):
            return False
        cnt_s, cnt_p = {}, {}
        for i in range(len(pattern)):
            pc, sc = pattern[i], s[i]
            if (pc in cnt_p and cnt_p[pc] != sc) or (sc in cnt_s and cnt_s[sc] != pc):
                return False
            cnt_p[pc], cnt_s[sc] = sc, pc
        return True
