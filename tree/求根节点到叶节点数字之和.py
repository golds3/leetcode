# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(root, sum):
            nonlocal ans
            if not root:
                return root
            if not root.left and not root.right:
                ans += sum + root.val
                return
            dfs(root.left, (sum + root.val) * 10)
            dfs(root.right, (sum + root.val) * 10)

        dfs(root, 0)
        return ans
