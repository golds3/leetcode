class Solution:
    def intToRoman(self, num: int) -> str:
        ans = []
        hash = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        for n, v in hash:
            while num >= n:
                num -= n
                ans.append(v)
            if num <= 0:
                break
        return ''.join(ans)


if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(3749))