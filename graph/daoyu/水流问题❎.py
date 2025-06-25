from typing import List



class Soution:
    """
    可以反过来
    从第一个边界逆流而上标记一组可以到达第一边界的节点
    从第二个边界逆流而上标记一组可以到达第二边界的节点
    最后相交的部分就是要求的节点
    """

    def fn(self, grid: List[List[int]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        destination = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(x, y, record):
            for v in destination:
                next_x, next_y = x + v[0], y + v[1]
                if next_x < 0 or next_x >= len(grid) or next_y < 0 or next_y >= len(grid[0]):
                    continue
                if not visited[next_x][next_y] and grid[next_x][next_y]>=grid[x][y]:
                    visited[next_x][next_y] = True
                    record.add((next_x, next_y))
                    dfs(next_x, next_y, record)

        # 第一个边界
        fr = set()
        for i in range(len(grid)):
            if  not visited[i][0]:
                visited[i][0] = True
                fr.add((i, 0))
                dfs(i, 0, fr)
        for j in range(len(grid[0])):
            if  not visited[0][j]:
                visited[0][j] = True
                fr.add((0, j))
                dfs(0, j, fr)
        # 第二个边界
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        sr = set()
        for i in range(len(grid)):
            if  not visited[i][-1]:
                visited[i][-1] = True
                sr.add((i, len(grid[0])-1))
                dfs(i, len(grid[0])-1, sr)
        for j in range(len(grid[0])):
            if  not visited[-1][j]:
                visited[-1][j] = True
                sr.add((len(grid)-1, j))
                dfs(len(grid)-1, j, sr)
        res = fr & sr
        for x,y in res:
            print(f"{x} {y}")


if __name__ == '__main__':
    s = Soution()
    while True:
        try:
            n, m = map(int, input().split())
            grid = [list(map(int, input().split())) for _ in range(n)]
            s.fn(grid)
        except Exception as e:
            break
