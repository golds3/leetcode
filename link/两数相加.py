# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        c = 0
        dummy = ListNode()
        tmp = dummy
        while l1 or l2 or c:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + c
            c, v = divmod(total, 10)
            tmp.next = ListNode(v)
            tmp = tmp.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
