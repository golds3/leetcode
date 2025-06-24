from collections import deque


class MyStack:

    def __init__(self):
        self.queue = deque()
        self.queue_back = deque()
    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        while len(self.queue) > 1:
            self.queue_back.append(self.queue.popleft())
        ans = self.queue.pop()
        tmp = self.queue
        self.queue = self.queue_back
        self.queue_back = tmp
        return ans
    def top(self) -> int:
        if self.empty():
            return None
        while len(self.queue) > 1:
            self.queue_back.append(self.queue.popleft())
        ans = self.queue.pop()
        self.queue_back.append(ans)
        tmp = self.queue
        self.queue = self.queue_back
        self.queue_back = tmp
        return ans
    def empty(self) -> bool:
        return not self.queue

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()