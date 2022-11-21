from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 1
        self.storage = [""] * (n + 2)

    def insert(self, idKey: int, value: str) -> List[str]:
        if idKey != self.ptr:
            self.storage[idKey] = value
            return []
        else:
            res = []
            self.storage[idKey] = value
            while self.storage[self.ptr] != "":
                res.append(self.storage[self.ptr])
                self.ptr += 1
            return res

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
