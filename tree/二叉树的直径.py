# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # max（左右子树最大深度之和）
        ans = 0

        def dfs(root):
            nonlocal ans
            if not root:
                return 0
            left_deep = dfs(root.left)
            right_deep = dfs(root.right)
            ans = max(ans, left_deep + right_deep)
            return max(left_deep, right_deep) + 1

        dfs(root)
        return ans
