class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                n = board[i][j]
                if n != ".":
                    if n in rows[i] or n in cols[j] or n in boxs[i // 3][j // 3]:
                        return False
                    rows[i].add(n)
                    cols[j].add(n)
                    boxs[i // 3][j // 3].add(n)
        return True
