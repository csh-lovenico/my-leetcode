import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.intervals = [0] * (len(w) + 1)
        for i in range(len(w)):
            self.intervals[i + 1] = self.intervals[i] + w[i]

    def pickIndex(self) -> int:
        def binary_search(x: int):
            upper = len(self.intervals) - 1
            lower = 0
            while lower < upper:
                mid = (lower + upper + 1) // 2
                if x <= self.intervals[mid]:
                    upper = mid - 1
                else:
                    lower = mid
            return lower

        random_index = random.randint(1, self.intervals[-1])
        return binary_search(random_index)


if __name__ == '__main__':
    s = Solution([1,3])
    for i in range(50):
        print(s.pickIndex())
