# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    """
    前缀树
    """

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        pre_sum = defaultdict(int)
        pre_sum[0] = 1 # 根节点路径
        def dfs(root, cur_sum):
            nonlocal ans
            if not root:
                return
            cur_sum+=root.val
            ans+=pre_sum[cur_sum-targetSum]
            pre_sum[cur_sum]+=1
            dfs(root.left, cur_sum)
            dfs(root.right, cur_sum)
            pre_sum[cur_sum]-=1

        dfs(root, 0)
        return ans


if __name__ == '__main__':
    s = Solution()
