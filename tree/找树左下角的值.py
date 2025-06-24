# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 先序遍历找到最大深度
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.max_dp = 0

        def dfs(node, deep):
            if not node:
                return
            if deep > self.max_dp and not node.left and not node.right:
                self.ans = node.val
                self.max_dp = deep
                return
            dfs(node.left, deep + 1)
            dfs(node.right, deep + 1)
            return

        dfs(root, 1)
        return self.ans

    # 层序遍历
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                ans = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans
