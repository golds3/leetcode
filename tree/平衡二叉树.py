# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # 左右节点的高度---求高度，需要后序遍历
        return self.dfs(root)!=-1

    def dfs(self,node)->int:
        if not node:
            return 0
        lh = self.dfs(node.left)
        if lh==-1:
            return -11
        rh = self.dfs(node.right)
        if rh==-1:
            return -1
        if abs(lh-rh)>1:
            return -1
        return 1+max(lh, rh)



