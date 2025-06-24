class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    # https://leetcode.cn/problems/design-linked-list/
    # 使用虚拟节点，比双链表要方便许多
    def __init__(self):
        self.dummy = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        tmp = self.dummy.next  # 这里取next，方便取值
        for i in range(index):
            tmp = tmp.next
        return tmp.val

    def addAtHead(self, val: int) -> None:
        self.dummy.next = ListNode(val=val,next=self.dummy.next)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        tmp = self.dummy
        while tmp.next:
            tmp = tmp.next
        tmp.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        tmp = self.dummy
        for i in range(index):
            tmp = tmp.next
        tmp.next = ListNode(val, tmp.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        tmp = self.dummy
        for i in range(index):
            tmp = tmp.next
        tmp.next = tmp.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)