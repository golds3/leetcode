# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r:
            return root
        if not l:
            return r
        return l

        # 回溯

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        queue = deque([root])
        hash = {root: None}
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    hash[node.left] = node
                    queue.append(node.left)
                if node.right:
                    hash[node.right] = node
                    queue.append(node.right)
            if p in hash and q in hash:
                break
        q_parent = {}
        while q:
            q_parent[q] = True
            q = hash[q]

        while p:
            if p in q_parent:
                return p
            p = hash[p]
        return None
