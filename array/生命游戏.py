from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # snapshot 不能改，一起变化
        def neary_cells(x, y):
            """
            x,y 附近的活细胞
            """
            dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            cells = 0
            for xx, yy in dir:
                cur_x, cur_y = x + xx, y + yy
                if (
                    cur_x >= 0
                    and cur_x < len(board)
                    and cur_y >= 0
                    and cur_y < len(board[0])
                ):
                    if board[cur_x][cur_y] == 1 or board[cur_x][cur_y] == 3:
                        cells += 1
            return cells

        # change_list = []
        # 定义board[i][j] = 2，表示发生0->1，board[i][j] = 3，表示发生1->0,取代额外空间change_list
        for i in range(len(board)):
            for j in range(len(board[0])):
                cells = neary_cells(i, j)
                if board[i][j] == 0 and cells == 3:
                    board[i][j] = 2
                    continue
                if board[i][j] == 1 and (cells < 2 or cells > 3):
                    board[i][j] = 3

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                if board[i][j] == 3:
                    board[i][j] = 0
