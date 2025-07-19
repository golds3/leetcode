# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        def dfs(root):
            """经过root的最大路径和"""
            nonlocal ans
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            child_max = max(left,right)
            cur_max = max(root.val,root.val+child_max) #左右二选一
            ans = max(ans,cur_max,left+right+root.val)
            return cur_max
        dfs(root)
        return ans