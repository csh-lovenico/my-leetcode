import heapq


# https://leetcode.com/problems/find-median-from-data-stream/discuss/2382589/Python-or-Heap-or-Time-Complexity-%3A-O(logn)
class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # store the numbers into two heaps, one min heap and one max heap
        # min heap (self.large) stores the numbers larger than the median
        # max heap (self.small) stores the numbers smaller than the median
        # so the median can be got from the tops of the heaps
        heapq.heappush(self.small, -1 * num)
        if (self.small and self.large) and self.small[0] * -1 > self.large[0]:
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)
        if len(self.small) > len(self.large):
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, val * -1)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        if len(self.large) > len(self.small):
            return self.large[0]
        return (self.small[0] * -1 + self.large[0]) / 2
