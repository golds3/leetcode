class ListNode:
    def __init__(self, val=0, next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:
    # 采用双向查找，效率比单向链表高
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        if index < self.size//2:
            tmp = self.head
            for i in range(index):
                tmp = tmp.next
        else:
            tmp = self.tail
            for i in range(self.size-index-1):
                tmp = tmp.prev
        return tmp.val
    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val,next=self.head)
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.size+=1


    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val,prev=self.tail)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            return
        if index ==0:
            self.addAtHead(val)
        elif index==self.size:
            self.addAtTail(val)
        else:
            if index<self.size//2:
                tmp = self.head
                for i in range(index-1):
                    tmp = tmp.next
            else:
                tmp = self.tail
                for i in range(self.size-index):
                    tmp = tmp.prev
            new_node = ListNode(val,prev=tmp,next=tmp.next)
            tmp.next = new_node
            new_node.next.prev = new_node
            self.size+=1


    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return
        if index==0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        elif index == self.size-1:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
        else:
            if index<self.size//2:
                tmp = self.head
                for i in range(index):
                    tmp = tmp.next
            else:
                tmp = self.tail
                for i in range(self.size-index-1):
                    tmp = tmp.prev
            tmp.prev.next = tmp.next
            tmp.next.prev = tmp.prev
        self.size-=1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)