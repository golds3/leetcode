# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 层序遍历
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        if not root:
            return ans
        queue = deque([root])
        while queue:
            sum = 0
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(sum/n)
        return ans
