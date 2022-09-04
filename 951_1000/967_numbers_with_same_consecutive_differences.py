import collections
from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        queue = collections.deque()
        result = []
        for i in range(1, 10):
            queue.append((i, 1))
        while queue:
            num, digit = queue.popleft()
            if digit == n:
                result.append(num)
                continue
            else:
                last_d = num % 10
                big_k = last_d + k
                if big_k < 10:
                    queue.append((num * 10 + big_k, digit + 1))
                small_k = last_d - k
                if 0 <= small_k != big_k:
                    queue.append((num * 10 + small_k, digit + 1))
        return result

