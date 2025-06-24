# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    #递归法
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        tmp = head
        new_head = self.swapPairs(head.next.next)
        node = tmp.next
        node.next = tmp
        tmp.next = new_head
        return node
    # 迭代版
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev,cur = dummy,dummy.next
        while cur and cur.next:
            next = cur.next.next
            prev.next = cur.next
            cur.next.next = cur
            cur.next = next
            prev = cur
            cur = next
        return dummy.next



