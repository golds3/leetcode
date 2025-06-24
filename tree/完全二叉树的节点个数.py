# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 因为是一个完全二叉树，可以考虑使用二叉树的性质，降低复杂度 满二叉树的节点个数 n = 2^l - 1
    # 在完全二叉树中，如果递归向左遍历的深度等于递归向右遍历的深度，那说明就是满二叉树
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        deep = 1
        left, right = root.left, root.right
        while left and right:
            deep += 1
            left, right = left.left, right.right
        if not left and not right:
            return 2 ** deep - 1
        return self.countNodes(root.left) + self.countNodes(root.right)+1

if __name__ == '__main__':
    so = Solution()
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.right = TreeNode(3)
    print(so.countNodes(r))
