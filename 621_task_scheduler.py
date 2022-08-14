from collections import deque, defaultdict
from heapq import heappush, heappop
from typing import List


# https://leetcode.com/problems/task-scheduler/discuss/2391297/Python-Solution-Using-Max-Heap-and-Queue-or-Time-Complexity%3A-O(n)-or-Space-Complexity%3A-O(n)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_heap = []
        queue = deque()
        word_count = defaultdict(int)
        timer = 0
        for i in range(len(tasks)):
            word_count[tasks[i]] += 1
        # no need to track each task's amount, only record their numbers and pick the most one
        for _, val in word_count.items():
            heappush(max_heap, -1 * val)
        while max_heap or queue:
            timer += 1
            if max_heap:
                # get the largest number and minus 1
                v = -1 * heappop(max_heap)
                v -= 1
                if v:
                    # the next time this task can be executed
                    queue.append((v, timer + n))
            # if the queue is not null and the first item in the queue can be executed at this time
            if queue and queue[0][1] == timer:
                # put the task in the heap
                heappush(max_heap, -1 * queue.popleft()[0])
        return timer
