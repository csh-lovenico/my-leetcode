import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-i for i in stones]
        heapq.heapify(heap)
        while len(heap) >= 2:
            s1 = -heapq.heappop(heap)
            s2 = -heapq.heappop(heap)
            if s1 == s2:
                continue
            else:
                heapq.heappush(heap, -abs(s1 - s2))
                continue
        if len(heap) == 1:
            return -heapq.heappop(heap)
        else:
            return 0
