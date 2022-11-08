import collections
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if not bank:
            return -1

        def diff(s1: str, s2: str) -> int:
            res = 0
            for i in range(8):
                if s1[i] != s2[i]:
                    res += 1
            return res

        visited = set()
        queue = collections.deque()
        # bfs
        queue.append((start, 0))
        while queue:
            curr, step = queue.popleft()
            if curr == end:
                return step
            visited.add(curr)
            for g in bank:
                if g not in visited and diff(curr, g) == 1:
                    queue.append((g, step + 1))

        return -1
