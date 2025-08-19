from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        旋转90度
        (i,j)-->(j,n-1-i)
        两步实现
        1.转置 (i,j)-->(j,i)
        2.行翻转(j,i)-->(j,n-1-i) --revserse
        """
        # step 1
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # step 2
        for row in matrix:
            row.reverse()
