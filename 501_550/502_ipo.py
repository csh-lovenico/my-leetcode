import heapq
from typing import List


# https://leetcode.com/problems/ipo/solutions/345371/python-greedy-pq-heap-o-nlogn/
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # find all available capitals now and pick the one that has the highest profit
        tasks = list(zip(capital, profits))
        # sort tasks by capital
        tasks.sort(key=lambda x: x[0])
        pq = []
        index = 0
        while k:  # O(NlogN) since we use 'index' to track the position, we only need to loop 'task' once
            for i in range(index, len(profits)):
                if tasks[i][0] <= w:
                    heapq.heappush(pq, (-tasks[i][1]))
                    index = i + 1
                else:
                    break
            if not pq:
                break
            w += -heapq.heappop(pq)
            k -= 1
        return w
