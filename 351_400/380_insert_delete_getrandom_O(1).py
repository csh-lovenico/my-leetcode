import random


# ac but slow
class RandomizedSet:

    def __init__(self):
        self.num_set = set()
        self.set_length = 0

    def insert(self, val: int) -> bool:
        if val in self.num_set:
            return False
        else:
            self.num_set.add(val)
            self.set_length += 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.num_set:
            self.num_set.remove(val)
            self.set_length -= 1
            return True
        else:
            return False

    def getRandom(self) -> int:
        return list(self.num_set)[random.randint(0, self.set_length - 1)]
