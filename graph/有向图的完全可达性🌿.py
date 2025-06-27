from collections import deque
from typing import List


class Solution:
    def fn(self,grid:List[List[int]]) -> int:
        visited = [False]*len(grid) #只要visited全部变成true，就说明可以到达所有地方
        visited[0],visited[1] = True,True
        def dfs(cur):
            for v in grid[cur]:
                if not visited[v]:
                    visited[v] =True
                    dfs(v)
        dfs(1)
        for v in visited:
            if not v:
                return -1
        return 1

    def fn_bfs(self,grid:List[List[int]]) -> int:
        visited = [False]*len(grid) #只要visited全部变成true，就说明可以到达所有地方
        visited[0],visited[1] = True,True
        q = deque([1])
        def bfs(cur):
            while q:
                cur = q.popleft()
                for v in grid[cur]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
        bfs(1)
        for v in visited:
            if not v:
                return -1
        return 1


if __name__ == '__main__':
    so = Solution()
    while True:
        try:
            n,edge = map(int,input().split())
            grid = [[] for _ in range(n+1)]
            for _ in range(edge):
                f,t = map(int,input().split())
                grid[f].append(t)
            print(so.fn_bfs(grid))

        except  EOFError as e:
            break