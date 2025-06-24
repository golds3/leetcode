from typing import List


# class Solution:
#     def solveSudoku(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         # 这个方法会超时
#         def is_valid(row, col, val):
#             if str(val) in board[row]:
#                 return False
#             for i in range(9):
#                 if board[i][col] == str(val):
#                     return False
#             row_end, col_end = 3 * (row // 3 + 1), 3 * (col // 3 + 1)
#             row_start, col_start = row_end - 3, col_end - 3
#             for i in range(row_start, row_end):
#                 for j in range(col_start, col_end):
#                     if board[i][j] == str(val):
#                         return False
#             return True
#
#         def is_vaild_new():
#
#         def dfs():
#             # 皇后每一行只需要放一个，但是这里每一样需要放多个，所以行也要从头遍历
#             for row in range(9):
#                 for col in range(9):
#                     if board[row][col] == '.':
#                         for i in range(1, 10):
#                             if is_valid(row, col, i):
#                                 board[row][col] = str(i)
#                                 if dfs():
#                                     return True
#                                 board[row][col] = '.'
#                         return False
#             return True
#
#         dfs()

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        all_set = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [[set() for _ in range(3)] for _ in range(3)]
        to_list = [] #需要填充的个数

        for i in range(9):
            for j in range(9):
                ch = board[i][j]
                if ch == ".":
                    to_list.append((i, j))
                else:
                    row_sets[i].add(ch)
                    col_sets[j].add(ch)
                    box_sets[i // 3][j // 3].add(ch)

        def dfs(curr):
            # 如果全部填充完了
            if curr == len(to_list):
                return True
            i, j = to_list[curr]
            # 对于(i,j)可以选择的数
            rest_set = all_set - row_sets[i] - col_sets[j] - box_sets[i // 3][j // 3]
            if not rest_set:
                return False

            for num in rest_set:
                board[i][j] = num
                row_sets[i].add(num)
                col_sets[j].add(num)
                box_sets[i // 3][j // 3].add(num)
                if dfs(curr + 1):
                    return True
                row_sets[i].remove(num)
                col_sets[j].remove(num)
                box_sets[i // 3][j // 3].remove(num)
            return False
        dfs(0)



if __name__ == '__main__':
    s = Solution()
    print(s.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))



