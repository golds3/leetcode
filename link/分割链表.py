# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        维护两个链表头，一个是小于x的，一个是>=x的然后吧两个链表拼接
        """
        small_dummy, big_dummy = ListNode(0), ListNode(0)
        s, b = small_dummy, big_dummy
        while head:
            if head.val < x:
                s.next = head
                head, s = head.next, s.next
            else:
                b.next = head
                b, head = b.next, head.next
        s.next = big_dummy.next
        b.next = None
        return small_dummy.next

    def partition_2(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(-101, head)
        slow, fast = dummy, dummy
        while fast and fast.next:
            if fast.val < x and fast.next.val < x:
                fast = fast.next
                slow = slow.next
            elif fast.next.val < x and fast.val >= x:
                tmp = fast.next
                fast.next = fast.next.next
                tmp.next = slow.next
                slow.next = tmp
                slow = slow.next

            else:
                fast = fast.next
        return dummy.next


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1, ListNode(3, ListNode(2)))
    s.partition(head, 3)
