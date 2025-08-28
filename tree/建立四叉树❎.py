"""
# Definition for a QuadTree node.

"""


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


from typing import List


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        # todo 用前缀和优化判断是否相等？
        if all(all(val == grid[0][0] for val in row) for row in grid):
            return Node(grid[0][0], 1)
        if len(grid) == 2:
            node = Node(
                1,
                0,
                Node(grid[0][0], 1),
                Node(grid[0][1], 1),
                Node(grid[1][0], 1),
                Node(grid[1][1], 1),
            )
            return node

        node = Node(1, 0)
        mid = len(grid) // 2
        tl = [row[:mid] for row in grid[:mid]]
        tr = [row[mid:] for row in grid[:mid]]
        bl = [row[:mid] for row in grid[mid:]]
        br = [row[mid:] for row in grid[mid:]]
        node.topLeft = self.construct(tl)
        node.topRight = self.construct(tr)
        node.bottomLeft = self.construct(bl)
        node.bottomRight = self.construct(br)
        return node
