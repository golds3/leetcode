class Solution:
    def isHappy(self, n: int) -> bool:
        m = {}
        while n != 1:
            if n in m:
                return False
            m[n] = n
            nn = 0
            while n:
                nn+=(n%10)*(n%10)
                n = n//10
            n = nn
        return True
