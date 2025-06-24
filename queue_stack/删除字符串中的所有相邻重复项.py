class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for v in s:
            if stack and stack[-1] ==v:
                while stack and stack[-1] == v:
                    stack.pop()
            else:
                stack.append(v)
        return ''.join(stack)


if __name__ == '__main__':
    so = Solution()
    s = 'abbab'
    print(so.removeDuplicates(s))