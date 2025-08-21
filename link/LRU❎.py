class LRUCache:
    """
    方法拆分！！！
    """

    class Node:
        def __init__(self, key=0, val=0, next=None, pre=None):
            self.key = key  # 用于淘汰
            self.val = val
            self.next = next
            self.pre = pre

    def __init__(self, capacity: int):
        self.head_dummy = self.Node()
        self.tail_dummy = self.Node()
        self.head_dummy.next = self.tail_dummy
        self.tail_dummy.pre = self.head_dummy
        self.cap = capacity
        self.map = {}

    def _remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def _move_to_tail(self, node):
        node.pre = self.tail_dummy.pre
        node.next = self.tail_dummy
        self.tail_dummy.pre.next = node
        self.tail_dummy.pre = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        target_node = self.map[key]
        self._remove(target_node)
        self._move_to_tail(target_node)
        return target_node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key].val = value
            target_node = self.map[key]
            self._remove(target_node)
            self._move_to_tail(target_node)
        else:
            if len(self.map) >= self.cap:
                del self.map[self.head_dummy.next.key]
                self._remove(self.head_dummy.next)
            new_node = self.Node(key=key, val=value)
            self._move_to_tail(new_node)
            self.map[key] = new_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
