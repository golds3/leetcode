# Definition for a Node.
from collections import deque


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # 不是一个完全二叉树
    def connect(self, root: "Node") -> "Node":
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

    def connect_dfs(self, root: "Node") -> "Node":
        pre = {}  # 记录每一层的第一个左节点

        def dfs(root, depth):
            if not root:
                return
            if len(pre) == depth:
                pre[depth] = root
            else:
                pre[depth].next = root
                pre[depth] = root
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 0)
        return root
