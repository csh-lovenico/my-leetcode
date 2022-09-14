import heapq
from collections import defaultdict
from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        heap = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                hashmap[nums[i]] += 1
        for k, v in hashmap.items():
            heapq.heappush(heap, (-v, k))
        return heapq.heappop(heap)[1]
