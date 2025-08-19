from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 先记录第一行第一列的情况，避免被覆盖了
        r0, c0 = False, False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                c0 = True
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                r0 = True
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j], matrix[i][0] = 0, 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if r0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if c0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
