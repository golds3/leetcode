

from collections import deque, defaultdict
from typing import List


class Solution:
    """
    给定一个由 1（陆地）和 0（水）组成的矩阵，你最多可以将矩阵中的一格水变为一块陆地，在执行了此操作之后，矩阵中最大的岛屿面积是多少。

    岛屿面积的计算方式为组成岛屿的陆地的总数。岛屿是被水包围，并且通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设矩阵外均被水包围
    """

    def fn(self, grid: List[List[int]]) -> int:
        """
        1.先统计每一个岛屿的面积
        2.遍历每一个海洋，然后计算相邻的岛屿和，取最大值
        :param grid:
        :return:
        """
        ans = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        areas = defaultdict(int) # key 是岛屿编号，value是岛屿面积
        area_sum = 0
        def dfs(x,y,area_no):
            nonlocal area_sum
            for v in directions:
                next_x, next_y = x+v[0], y+v[1]
                if next_x<0 or next_x>=len(grid) or next_y<0 or next_y>=len(grid[0]):
                    continue
                if not visited[next_x][next_y] and grid[next_x][next_y]==1:
                    area_sum+=1
                    visited[next_x][next_y] = True
                    #把这块土地标记为区域
                    grid[next_x][next_y] =area_no
                    dfs(next_x,next_y,area_no)
        index = 2
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j]==1:
                    index+=1
                    area_sum = 1
                    visited[i][j] = True
                    grid[i][j] = index
                    dfs(i,j,index)
                    areas[index] = area_sum
                    ans = max(ans,area_sum)

        # 遍历水
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    tmp = 1
                    land = set()  # 记录选择过的岛屿
                    for v in directions:
                        next_x, next_y = i+v[0], j+v[1]
                        if next_x<0 or next_x>=len(grid) or next_y<0 or next_y>=len(grid[0]):
                            continue
                        if grid[next_x][next_y]>1 and grid[next_x][next_y] not in land:
                            tmp += areas[grid[next_x][next_y]]
                            land.add(grid[next_x][next_y])
                    ans = max(ans, tmp)
        return ans


if __name__ == '__main__':
    s = Solution()
    while True:
        try:
            n, m = map(int, input().split())
            grid = []
            for _ in range(n):
                grid.append(list(map(int, input().split())))
            print(s.fn(grid))
        except Exception as e:
            break
