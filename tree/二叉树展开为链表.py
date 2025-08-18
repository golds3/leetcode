# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    两种方法
    1。头插法
    2. 尾插法
    """

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        头插法 ——把左节点插入到右节点前面
        """
        pre = None  # 记录当前的右节点

        def dfs(root):
            nonlocal pre
            if not root:
                return
            dfs(root.right)
            dfs(root.left)
            # 把当前节点插入到右节点的前面 （头插法）
            root.right = pre
            root.left = None
            pre = root

        dfs(root)
        return root

    def flatten2(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        尾插法，把右节点插入到左节点右边
        """

        def getTail(root):
            """
            将root的节点拉成一条链表作为右节点
            返回链表的尾节点
            """
            if not root:
                return None
            left_tail = getTail(root.left)
            right_tail = getTail(root.right)
            if left_tail:
                # 把右节点插入到左边
                left_tail.right = root.right
                root.right = root.left
                root.left = None
            if right_tail:
                # 如果右子树存在尾节点，那么一定是链表的尾节点，因为上面已经插入到左节点右边了
                return right_tail
            if left_tail:
                return left_tail
            return root

        getTail(root)
        return root
