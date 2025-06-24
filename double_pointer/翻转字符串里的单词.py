class Solution:
    def reverseWords(self, s: str) -> str:
        #去除空格 --缩容，快慢指针
        s = self.modify(list(s))
        self.reverse(s,0,len(s)-1)
        left,right = 0,0
        for k,v in enumerate(s):
            if v==' ':
                right = k-1
                self.reverse(s,left,right)
                left = k+1
            if k ==len(s)-1:
                self.reverse(s,left,k)
        return ''.join(s)

    def reverse(self, s,left:int,right:int):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def modify(self, s:list[str])->list[str]:
        slow, fast = 0, 0
        while fast < len(s):
            if s[fast] != ' ':
                if slow != 0:
                    s[slow] = ' '
                    slow += 1
                while fast < len(s) and s[fast] != ' ':
                    s[slow] = s[fast]
                    slow += 1
                    fast += 1
            fast += 1
        s = s[:slow]
        return s


if __name__ == '__main__':
    so = Solution()
    print(so.reverseWords("   hello  world  "))
