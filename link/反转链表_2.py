# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if left == right or not head:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        # 1. 先走到 left-1 位置
        for _ in range(left - 1):
            pre = pre.next

        # 2. 反转区间
        cur = pre.next
        prev = None
        for _ in range(right - left + 1):
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        # 3. 拼接
        pre.next.next = cur  # 原 left 节点接到反转后面的部分
        pre.next = prev  # left-1 节点接到反转后的头

        return dummy.next

    def reverseBetween_dfs(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        def reverse(head, n):
            if n == 1:
                return head, head.next
            new_head, tail = reverse(head.next, n - 1)
            head.next.next = head
            head.next = tail
            return new_head

        if left == 1:
            # 从头反转
            new_head, _ = reverse(head, right)
            return new_head
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    s.reverseBetween(head, 2, 4)
