import collections


# ac but slow, use much fewer memories
class LRUCache:

    def __init__(self, capacity: int):
        self.least_queue = []
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
                key_to_delete = self.least_queue.pop(0)
                self.exist_map[key_to_delete] = 0
                self.kv_map[key_to_delete] = -1
                self.exist_map[key] = 1
                self.kv_map[key] = value
                self.least_queue.append(key)


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
