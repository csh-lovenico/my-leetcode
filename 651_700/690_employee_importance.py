import collections
from typing import List


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        queue = collections.deque()
        im = 0
        hashmap = dict()
        for e in employees:
            hashmap[e.id] = e
        queue.append(hashmap[id])
        while queue:
            curr = queue.popleft()
            im += curr.importance
            for sub in curr.subordinates:
                queue.append(hashmap[sub])

        return im
