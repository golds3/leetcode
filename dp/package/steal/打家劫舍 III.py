# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode])->List[int]:
            if not root:
                return [0,0]
            left = dfs(root.left)
            right = dfs(root.right)
            steal_cur = root.val + left[0]+right[0]
            not_steal_cur = max(left)+max(right)
            print([not_steal_cur,steal_cur])
            return [not_steal_cur,steal_cur]
        return max(dfs(root))


if __name__ == '__main__':
    so = Solution()
    r = TreeNode(4)
    r.left = TreeNode(1)
    r.left.left = TreeNode(2)
    r.left.left.left = TreeNode(3)
    print(so.rob(r))
