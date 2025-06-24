# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 层序遍历
    def minDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if not root:
            return ans
        queue = deque([root])
        while queue:
            ans+=1
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node.left and not node.right:
                    return ans
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans

    #dfs
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == right==0:
            return 1
        if left==0:
            return right+1
        if right==0:
            return left+1
        return min(left, right)+1

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.right.left = TreeNode(5)
    print(Solution().minDepth2(root))

