from typing import List


class Soution:
    def fn(self,grid:List[List[int]])->int:
        ans = 0
        destination = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        def dfs(x,y):
            nonlocal ans
            for v in destination:
                next_x,next_y = x+v[0],y+v[1]
                if next_x<0 or next_x>=len(grid) or next_y<0 or next_y>=len(grid[0]):
                    continue
                if not visited[next_x][next_y] and grid[next_x][next_y]==1:
                    visited[next_x][next_y] = True
                    ans+=1
                    dfs(next_x,next_y)
            return ans

        # 前把靠近边缘的岛屿都填充
        for i in range(len(grid)):
            if grid[i][0] == 1 and not visited[i][0]:
                visited[i][0] = True
                dfs(i,0)
        for i in range(len(grid)):
            if grid[i][-1] == 1 and not visited[i][-1]:
                visited[i][-1] = True
                dfs(i,len(grid[0])-1)
        for j in range(len(grid[0])):
            if grid[0][j] == 1 and not visited[0][j]:
                visited[0][j] = True
                dfs(0,j)
        for j in range(len(grid[0])):
            if grid[-1][j] == 1 and not visited[-1][j]:
                visited[-1][j] = True
                dfs(len(grid)-1,j)
        ans = 0
        # 剩下的都是孤岛
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                if grid[i][j] == 1 and not visited[i][j]:
                    visited[i][j] = True
                    ans+=1
                    dfs(i,j)
        return ans








if __name__ == '__main__':
    s = Soution()
    while True:
        try:
            n,m = map(int,input().split())
            grid = [list(map(int,input().split())) for _ in range(n)]
            print(s.fn(grid))
        except Exception as e:
            break