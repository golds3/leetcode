from collections import deque
from typing import Optional

"""
这题和下一个变题不同点在于树点类型，如果使用bfs解决，那么这两题没有区别
如果使用dfs就有区别了，满二叉树不需要考虑空点情况，而变形题则需要考虑
"""

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # 这是一颗满二叉树
    # 层序遍历
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        queue = deque([root])
        while queue:
            pre = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if pre:
                    pre.next = node
                pre = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root

