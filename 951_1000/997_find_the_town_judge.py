import collections
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_map = collections.defaultdict(int)
        out_map = collections.defaultdict(int)
        for t in trust:
            in_map[t[1]] += 1
            out_map[t[0]] += 1

        for i in range(1, n + 1):
            if in_map[i] == n - 1 and out_map[i] == 0:
                return i

        return -1
