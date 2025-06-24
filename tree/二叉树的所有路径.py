# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        tmp = []
        def dfs(node,cur):
            if not node:
                return
            cur += str(node.val)
            if not node.left and not node.right:
                tmp.append(cur)
                return
            dfs(node.left,cur+'->')
            dfs(node.right,cur+'->')
            return
        dfs(root,'')
        return tmp

if __name__ == '__main__':
    so = Solution()
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.right = TreeNode(3)
    print(so.binaryTreePaths(r))


