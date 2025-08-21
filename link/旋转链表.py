# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        n = 0
        cur = head
        tail = None
        while cur:
            if not cur.next:
                tail = cur
            n += 1
            cur = cur.next
        if k % n == 0:
            return head
        k %= n
        slow, cur = head, head
        for _ in range(k):
            cur = cur.next
        while cur and cur.next:
            cur = cur.next
            slow = slow.next
        new_head = slow.next
        slow.next = None
        tail.next = head
        return new_head
