# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    """
    array 保存了所有的node，O（n）的空间
    """

    def __init__(self, root: Optional[TreeNode]):
        self.array = []

        def get_order(root):
            if not root:
                return
            get_order(root.left)
            self.array.append(root.val)
            get_order(root.right)

        get_order(root)
        self.iterator = -1

    def next(self) -> int:
        ans = self.array[self.iterator + 1]
        self.iterator += 1
        return ans

    def hasNext(self) -> bool:
        return self.iterator < len(self.array) - 1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


class BSTIterator_v2:
    """
    不需要把所有节点顺序保存，只需要保存当前next所在的子BTS的顺序 按照左中🈶右的顺序，root节点需要保存h（高度）个--一路left
    """

    def __init__(self, root: Optional[TreeNode]):
        self.iterator = root
        self.stack = []

    def next(self) -> int:
        tmp = self.iterator
        while tmp:
            # 利用stack的后入先出--实现左中顺序
            self.stack.append(tmp)
            tmp = tmp.left
        ans, self.stack = self.stack[-1], self.stack[:-1]
        self.iterator = ans.right  # 右
        return ans.val

    def hasNext(self) -> bool:
        return self.iterator != None or len(self.stack) > 0
