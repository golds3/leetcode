from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        先用二分查找target在哪一行
        在用二分查找改行
        """
        left, right = 0, len(matrix)
        while left < right:
            mid = left + (right - left) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid
        row = left - 1
        if row < 0:
            return False
        left, right = 0, len(matrix[0])
        while left < right:
            mid = left + (right - left) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid
        return False
