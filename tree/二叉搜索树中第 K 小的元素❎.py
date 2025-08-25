# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    todo 如果root频繁修改呢？AVL解法？
    """

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0

        def dfs(root):
            nonlocal ans, k
            if not root:
                return None
            dfs(root.left)
            k -= 1
            if k == 0:
                ans = root.val
                return
            dfs(root.right)

        dfs(root)
        return ans
