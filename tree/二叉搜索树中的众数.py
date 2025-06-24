# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.ans = []
        self.pre = None
        self.count = 0
        self.max_count = 0

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return self.ans
        self.findMode(root.left)
        if self.pre and self.pre.val == root.val:
            self.count+=1
        else:
            self.count=1
        self.pre = root
        if self.count == self.max_count:
            self.ans.append(root.val)
        if self.count > self.max_count:
            self.max_count = self.count
            self.ans = [root.val]
        self.findMode(root.right)
        return self.ans
