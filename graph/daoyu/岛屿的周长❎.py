from collections import deque
from typing import List


class Solution:
    """
    这题和之前的不同，岛屿中的每一块都有作用--周长，所以不需要dfs/bfs来处理整体的岛屿
    有两种方案 以水的角度、以陆地的角度
    """
    def fn_1(self, grid: List[List[str]]) -> int:
        """
        如果一个陆块的附近是水、或者是边界，那么周长+1
        :param grid:
        :return:
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    for v in directions:
                        next_x, next_y = i+v[0], j+v[1]
                        if next_x<0 or next_x>=len(grid) or next_y<0 or next_y>=len(grid[0]) or grid[next_x][next_y] == '0':
                            ans+=1
        return ans

    def fn_2(self, grid: List[List[str]]) -> int:
        """
        一个陆块的周长是4，如果有一个相邻的陆块，那么周长要-2
        :param grid:
        :return:
        """
        #   向右或向下
        directions = [(0, 1), (1, 0)]
        land = 0
        cover = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    land+=1
                    for v in directions:
                        next_x, next_y = i+v[0], j+v[1]
                        if 0<=next_x<len(grid) and 0<=next_y<len(grid[0])and grid[next_x][next_y] == '1':
                            cover+=1
        return land*4-2*cover
if __name__ == '__main__':
    s = Solution()
    while True:
        try:
            n,m = map(int,input().split())
            grid = []
            for i in range(n):
                tmp = input().split()
                grid.append(tmp)
            print(s.fn_2(grid))
        except Exception as e:
            break
