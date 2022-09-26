class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.capacity = k
        self.size = 0
        self.head = 0
        # tail is the next place to be inserted, real tail is getPrev(tail)
        self.tail = 0

    def getNext(self, n: int) -> int:
        return (n + 1) % self.capacity

    def getPrev(self, n: int) -> int:
        n = n - 1
        if n < 0:
            n += self.capacity
        return n

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.queue[self.tail] = value
            self.tail = self.getNext(self.tail)
            self.size += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.head = self.getNext(self.head)
            self.size -= 1
            return True
        else:
            return False

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.getPrev(self.tail)]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
