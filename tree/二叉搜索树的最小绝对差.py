# Definition for a binary tree node.
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.ans = sys.maxsize
        self.pre = None
        def dfs(node:TreeNode):
            if not node:
                return
            dfs(node.left)
            if self.pre:
                self.ans = min(self.ans,node.val-self.pre.val)
            self.pre = node
            dfs(node.right)
        dfs(root)
        return self.ans

