from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def is_correct(start, end):
            if start > end:
                return False
            if s[start] == '0' and start != end:
                return False
            su = 0
            for i in range(start, end + 1):
                if not s[i].isdigit():
                    return False
                su = su * 10 + int(s[i])
                if su > 255:
                    return False
            return True

        def dfs(start: int, cur: str):
            if cur.count('.') == 3 and is_correct(start, len(s) - 1):
                cur += s[start:]
                ans.append(cur)
            for i in range(start, len(s)):
                if is_correct(start, i):
                    dfs(i + 1, cur + s[start:i + 1] + '.')

        dfs(0, '')
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.restoreIpAddresses("25525511135"))
