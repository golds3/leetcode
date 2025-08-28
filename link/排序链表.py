# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        slow.next = None
        head1 = self.sortList(dummy.next)
        head2 = self.sortList(right)
        new_head = ListNode(0)
        tmp = new_head
        while head1 and head2:
            if head1.val <= head2.val:
                tmp.next = ListNode(head1.val)
                head1 = head1.next
            else:
                tmp.next = ListNode(head2.val)
                head2 = head2.next
            tmp = tmp.next
        if head1:
            tmp.next = head1
        if head2:
            tmp.next = head2
        return new_head.next


if __name__ == "__main__":
    s = Solution()
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    s.sortList(head)
