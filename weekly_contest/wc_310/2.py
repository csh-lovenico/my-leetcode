import heapq
from collections import defaultdict


class Solution:
    def partitionString(self, s: str) -> int:
        letters = set()
        result = 1
        for i in range(len(s)):
            if s[i] not in letters:
                letters.add(s[i])
            else:
                result += 1
                letters = {s[i]}
        return result
