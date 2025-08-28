# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        head1 = self.mergeKLists(lists[:mid])
        head2 = self.mergeKLists(lists[mid:])
        dummy = ListNode()
        cur = dummy
        while head1 and head2:
            if head1.val <= head2.val:
                cur.next = ListNode(head1.val)
                head1 = head1.next
            else:
                cur.next = ListNode(head2.val)
                head2 = head2.next
            cur = cur.next
        if head1:
            cur.next = head1
        if head2:
            cur.next = head2
        return dummy.next
