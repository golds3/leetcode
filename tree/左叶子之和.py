# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 求和，使用后序遍历
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lv = 0
        if root.left and  not root.left.left and not root.left.right:
            lv = root.left.val
        return lv + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)


if __name__ == '__main__':
    s = Solution()
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.right = TreeNode(3)
    print(s.sumOfLeftLeaves(r))
