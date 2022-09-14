from heapq import heappush, heappop
from typing import List

# https://leetcode.com/problems/maximum-performance-of-a-team/discuss/2559880/Easiest-Python-approach-(explained)
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # variable zipped: stores employees' efficiency and speed in decreasing order of efficiency then speed
        zipped = sorted(zip(efficiency, speed), reverse=True)

        output = 0

        # initialise heap
        h = []

        # to store sum of employees' speed, initialise sm
        sm = 0

        # loop to iterate over zipped
        for z in range(0, n):

            # current employee's speed
            emp_speed = zipped[z][1]

            # current employee's efficiency
            emp_efficiency = zipped[z][0]

            # push employee speed to heap h
            heappush(h, emp_speed)

            # increament sm by current employee's speed, since we want to focus on maximising speed
            sm += emp_speed

            # if number of employees' speed in heap > k
            if len(h) > k:
                # subtract the popped heap node from sm
                sm -= heappop(h)

            # find maximum performance
            # emp_efficiency is already minimum as we sorted it before
            output = max(output, sm * emp_efficiency)

        return output % (10 ** 9 + 7)