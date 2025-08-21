"""
# Definition for a Node.
"""

from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.map = {}

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        """
        不使用hash数组
        A-B-C ===》 A-A'-B-B'-C-C'
        """
        if not head:
            return head
        cur = head
        while cur:
            copy_node = Node(cur.val, cur.next)
            cur.next = copy_node
            cur = cur.next.next
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        ans = head.next
        cur = head
        while cur:
            copy_node = cur.next
            cur.next = cur.next.next
            if copy_node.next:
                copy_node.next = copy_node.next.next
            cur = cur.next
        return ans

    def copyRandomList_v2(self, head: "Optional[Node]") -> "Optional[Node]":
        """
        迭代的话可以先遍历一次，创建节点（不构造next和random）放入hash，第二次遍历在构造next和random
        """
        if not head:
            return head
        if head in self.map:
            return self.map[head]
        copy_node = Node(head.val)
        self.map[head] = copy_node
        copy_node.next = self.copyRandomList(head.next)
        copy_node.random = self.copyRandomList(head.random)
        return copy_node
