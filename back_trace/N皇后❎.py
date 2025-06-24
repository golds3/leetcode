from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 行、列、主对角线、斜对角线
        ans = []
        tmp = ['.'*n for _ in range(n)]
        def is_valid(row,col):
            #列
            for i in range(row):
                if tmp[i][col] == 'Q':
                    return False
            # 主对角线
            i,j = row-1,col-1
            while i>=0 and j>=0:
                if tmp[i][j]=='Q':
                    return False
                i-=1
                j-=1
            # 反对角线
            i,j = row-1,col+1
            while i>=0 and j<n:
                if tmp[i][j]=='Q':
                    return False
                i-=1
                j+=1
            return True
        def dfs(row:int):
            #如果能遍历到叶子节点，就说明方案可行
            if row == n:
                ans.append(tmp[:])
                return
            for col in range(n):
                if is_valid(row,col):
                    tmp[row] = tmp[row][:col] + 'Q' +tmp[row][col+1:]
                    dfs(row+1)
                    tmp[row] = tmp[row][:col] + '.' +tmp[row][col+1:]

        dfs(0)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(4))

