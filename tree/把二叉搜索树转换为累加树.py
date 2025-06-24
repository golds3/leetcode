# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pre = 0
        def dfs(root:TreeNode):
            nonlocal pre
            if not root:
                return
            dfs(root.right)
            root.val += pre
            pre = root.val
            dfs(root.left)
            return
        dfs(root)
        return root