class Solution:
    def __init__(self) -> None:
        self.ans = []
        self.map = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

    def letterCombinations(self, digits: str) -> list[list[int]]:
        if not digits:
            return []
        ans = []
        def dfs(start:int,cur:str):
            nonlocal ans
            if len(cur) == len(digits):
                ans.append(cur)
                return
            curS = self.map[digits[start]]
            for v in curS:
                dfs(start+1,cur+v)
        dfs(0,"")
        return ans if ans else []