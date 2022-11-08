import collections


# ac but slow, use much fewer memories
class LRUCache:

    def __init__(self, capacity: int):
        # the queue may use a double linked list to implement
        self.least_queue = collections.deque()
        self.capacity = capacity
        self.kv_map = collections.defaultdict(lambda: -1)
        self.exist_map = [0] * 10001

    def get(self, key: int) -> int:
        if self.exist_map[key] == 1:
            self.least_queue.remove(key)
            self.least_queue.append(key)
            return self.kv_map[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.least_queue) < self.capacity:
            if self.exist_map[key] == 1:
                self.kv_map[key] = value
                self.least_queue.remove(key)
                self.least_queue.append(key)
            else:
                self.exist_map[key] = 1
                self.kv_map[key] = value
                self.least_queue.append(key)
        else:
            if self.exist_map[key] == 1:
                self.kv_map[key] = value
                self.least_queue.remove(key)
                self.least_queue.append(key)
            else:
                key_to_delete = self.least_queue.popleft()
                self.exist_map[key_to_delete] = 0
                self.kv_map[key_to_delete] = -1
                self.exist_map[key] = 1
                self.kv_map[key] = value
                self.least_queue.append(key)


# Double linked list
class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCacheLinkedList:
    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0
        self.ketToNode = dict()

    def addToTail(self, key, val):
        node = Node(key, val)
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.ketToNode[key] = node
        self.size += 1

    def delete(self, key):
        node = self.ketToNode[key]
        del self.ketToNode[key]
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        self.size -= 1

    def get(self, key: int) -> int:
        if key not in self.ketToNode:
            return -1

        value = self.ketToNode[key].val
        self.delete(key)
        self.addToTail(key, value)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.ketToNode:
            self.delete(key)
            self.addToTail(key, value)
            return

        if self.size == self.capacity:
            self.delete(self.head.next.key)

        self.addToTail(key, value)


# another solution using Python features
# https://leetcode.com/problems/lru-cache/discuss/2361512/Python-Dictionary-Without-Ordered-Dictionary
class LRUCacheDict:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.data = {}

    def get(self, key: int) -> int:
        if key not in self.data: return -1
        # item recently accessed need to be sent at last of dict, pop and reassign
        self.data[key] = self.data.pop(key)
        return self.data[key]

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            # item updated recently need to be sent at last of dict, pop and update
            self.data.pop(key)
            self.data[key] = value
            return
        # if capacity is reached, we removed first item of dict. which is always least used
        if self.cap == len(self.data): self.data.pop(next(iter(self.data)))
        self.data[key] = value
        return


if __name__ == '__main__':
    s = LRUCache(2)
    s.put(1, 1)
    s.put(2, 2)
    print(s.get(1))
    s.put(3, 3)
    print(s.get(2))
