from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for _ in range(n)] for _ in range(n)]
        cur = 1
        up,down,right,left = 0,n-1,n-1,0
        while left<=right and up<=down:
            for i in range(left,right+1):
                ans[up][i] = cur
                cur+=1
            up+=1
            for i in range(up,down+1):
                ans[i][right] = cur
                cur+=1
            right-=1
            if up<=down:
                for i in range(right,left-1,-1):
                    ans[down][i] = cur
                    cur+=1
                down-=1
            if left<=right:
                for i in range(down,up-1,-1):
                    ans[i][left] = cur
                    cur+=1
                left+=1
        return ans