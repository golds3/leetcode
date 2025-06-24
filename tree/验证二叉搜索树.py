# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def __init__(self):
        self.pre = None

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        l = self.isValidBST(root.left)
        if not l:
            return False
        if self.pre and self.pre.val >= root.val:
            return False
        self.pre = root
        return self.isValidBST(root.right)
