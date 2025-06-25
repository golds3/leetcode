from typing import List


class Soution:

    """
    也可以不用visited辅组数组
    先把靠边的岛屿设置为2
    然后遍历整个grid，值为2的改成1，为1的置为0
    """
    def fn(self,grid:List[List[int]])->int:
        destination = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        def dfs(x,y,flag=True):
            for v in destination:
                next_x,next_y = x+v[0],y+v[1]
                if next_x<0 or next_x>=len(grid) or next_y<0 or next_y>=len(grid[0]):
                    continue
                if not visited[next_x][next_y] and grid[next_x][next_y]==1:
                    if flag:
                        visited[next_x][next_y] = True
                        dfs(next_x,next_y)
                    else:
                        visited[next_x][next_y] = True
                        grid[next_x][next_y] = 0
                        dfs(next_x,next_y,False)

        # 前把靠近边缘的岛屿都填充
        for i in range(len(grid)):
            if grid[i][0] == 1 and not visited[i][0]:
                visited[i][0] = True
                dfs(i,0)
            if grid[i][-1] == 1 and not visited[i][-1]:
                visited[i][-1] = True
                dfs(i,len(grid[0])-1)
        for j in range(len(grid[0])):
            if grid[0][j] == 1 and not visited[0][j]:
                visited[0][j] = True
                dfs(0,j)
            if grid[-1][j] == 1 and not visited[-1][j]:
                visited[-1][j] = True
                dfs(len(grid)-1,j)
        # 剩下的都是孤岛
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                if grid[i][j] == 1 and not visited[i][j]:
                    visited[i][j] = True
                    grid[i][j] = 0
                    dfs(i,j,False)

        for v in grid:
            print(' '.join(map(str,v)))






if __name__ == '__main__':
    s = Soution()
    while True:
        try:
            n,m = map(int,input().split())
            grid = [list(map(int,input().split())) for _ in range(n)]
            s.fn(grid)
        except Exception as e:
            break