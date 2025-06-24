import operator
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def div(x,y):
            return x//y if x * y > 0 else -(abs(x) // abs(y))
        map = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': div}
        stack = []
        for v in tokens:
            if v in map:
                if len(stack) < 2:
                    return 0
                sec, fir = stack.pop(), stack.pop()
                stack.append(map[v](fir, sec))
            else:
                stack.append(int(v))
        return stack.pop()
if __name__ == '__main__':
    so = Solution()
    print(so.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))