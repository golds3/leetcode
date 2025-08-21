# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0, head)
        slow, fast = dummy, head.next
        while fast:
            if slow.next.val == fast.val:
                while fast and fast.val == slow.next.val:
                    fast = fast.next
                slow.next = fast
                if fast:
                    fast = fast.next
                continue
            slow = slow.next
            fast = fast.next
        return dummy.next


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1, ListNode(1, ListNode(2, ListNode(3))))
    s.deleteDuplicates(head)
