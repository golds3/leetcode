from collections import Counter, defaultdict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 双向映射
        cnt_s, cnt_t = {}, {}
        for i in range(len(s)):
            sc, tc = s[i], t[i]
            if sc in cnt_s and cnt_s[sc] != tc or (tc in cnt_t and cnt_t[tc] != sc):
                return False
            cnt_s[sc], cnt_t[tc] = tc, sc
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isIsomorphic("add", "egg"))
