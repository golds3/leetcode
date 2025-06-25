from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(x,y):
            for v in directions:
                next_x, next_y = x+v[0], y+v[1]
                if next_x<0 or next_x>=len(grid) or next_y<0 or next_y>=len(grid[0]):
                    continue
                if grid[next_x][next_y]=='1' and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    dfs(next_x,next_y)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1' and not visited[i][j]:
                    visited[i][j] = True
                    ans+=1
                    #把相邻的陆地遍历完
                    dfs(i,j)
        return ans


    def numIslands_bfs(self, grid: List[List[str]]) -> int:
        ans = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(x, y):
            q = deque([(x, y)])
            while q:
                cur_x,cur_y = q.popleft()
                for v in directions:
                    next_x, next_y = cur_x+v[0], cur_y+v[1]
                    if next_x<0 or next_x>=len(grid) or next_y<0 or next_y>=len(grid[0]):
                        continue
                    if grid[next_x][next_y]=='1' and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        q.append((next_x, next_y))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    visited[i][j] = True
                    ans += 1
                    # 把相邻的陆地遍历完
                    bfs(i, j)
        return ans


if __name__ == '__main__':
    s = Solution()
    while True:
        try:
            n,m = map(int,input().split())
            grid = []
            for i in range(n):
                tmp = input().split()
                grid.append(tmp)
            print(s.numIslands_bfs(grid))
        except Exception as e:
            break
