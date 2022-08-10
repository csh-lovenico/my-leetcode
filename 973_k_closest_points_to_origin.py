import heapq
import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        queue = []
        heapq.heapify(queue)
        for i in range(k):
            distance = math.sqrt(math.pow(points[i][0], 2) + math.pow(points[i][1], 2))
            # heap operations will pop the smallest item, so revert the distance
            # use -distance might be also ok
            if distance != 0:
                item = (1 / distance, points[i])
            else:
                item = (999999, points[i])
            heapq.heappush(queue, item)
        for i in range(k, len(points)):
            distance = math.sqrt(math.pow(points[i][0], 2) + math.pow(points[i][1], 2))
            if distance != 0:
                item = (1 / distance, points[i])
            else:
                item = (999999, points[i])
            heapq.heappushpop(queue, item)
        result = []
        for i in range(len(queue)):
            result.append(heapq.heappop(queue)[1])
        return result
