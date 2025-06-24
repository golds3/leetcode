class Solution:
    def isValid(self, s: str) -> bool:
        map = {'}':'{',')':'(',']':'['}
        stack = []
        for v in s:
            if v in map:
                if not stack or stack[-1]!=map[v]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(v)
        return not stack
