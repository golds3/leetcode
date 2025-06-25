from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        tmp = 0
        def dfs(x,y):
            nonlocal tmp
            for v in directions:
                new_x, new_y = x+v[0], y+v[1]
                if new_x<0 or new_x>=len(grid) or new_y<0 or new_y>=len(grid[0]):
                    continue
                if grid[new_x][new_y]==1 and not visited[new_x][new_y]:
                    visited[new_x][new_y] = True
                    tmp += 1
                    dfs(new_x,new_y)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j]==1:
                    visited[i][j] = True
                    tmp = 1
                    dfs(i,j)
                    ans = max(ans, tmp)
        return ans

    def maxAreaOfIsland_bfs(self, grid: List[List[int]]) -> int:
        ans = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        tmp = 0
        def bfs(x,y):
            q = deque([(x,y)])
            nonlocal tmp
            while q:
                cur_x, cur_y = q.popleft()
                for v in directions:
                    next_x, next_y = cur_x + v[0], cur_y + v[1]
                    if next_x<0 or next_x>=len(grid) or next_y<0 or next_y>=len(grid[0]):
                        continue
                    if grid[next_x][next_y]==1 and not visited[next_x][next_y]:
                        tmp+=1
                        visited[next_x][next_y] = True
                        q.append((next_x,next_y))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j]==1:
                    visited[i][j] = True
                    tmp = 1
                    bfs(i,j)
                    ans = max(ans, tmp)
        return ans



if __name__ == '__main__':
    s = Solution()
    while True:
        try:
            n,m = map(int,input().split())
            grid = [list(map(int,input().split())) for _ in range(n)]
            print(s.maxAreaOfIsland_bfs(grid))
        except Exception as e:
            break
