# Definition for an Interval.
from heapq import heappush, heappop
from typing import List


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


# similar to merging intervals
# https://leetcode.com/problems/employee-free-time/discuss/2140054/Super-Simple-Python-%2B-Detailed-Explanation-Builds-on-Merge-Interval-Prob
class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])  # O(NlogN)
        ranges = []

        for interval in intervals:
            if len(ranges) == 0 or ranges[-1][1] < interval[0]:
                ranges.append(interval)
            else:
                ranges[-1][1] = max(ranges[-1][1], interval[1])
        return ranges

    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        s = []
        # New Code for This Question
        # Convert to a standard list of lists or tuples
        for sch in schedule:
            for ranges in sch:
                s.append([ranges.start, ranges.end])

        # Call function/Code from Merge-Intervals Problem
        shifts = self.merge(s)
        free_time = []

        # New Code for this Question
        n = len(shifts)
        # Construct a Free Time interval based on the previous shift end & next shift start time
        for i in range(1, n):
            free_time.append(Interval(start=shifts[i - 1][1], end=shifts[i][0]))

        return free_time


# another solution using pq
# https://leetcode.com/problems/employee-free-time/discuss/2283456/What-they-ask-for-in-the-interviews-or-Python-heap-merge-k-lists-O(N*lgK)
class SolutionUsingHeap:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # Use PQ to merge k lists of sorted intervals O(NlgK)
        # While merging, track the previous interval pre
        # If pre does not overlap with curr, we found a gap and append it. Else, we update pre.end
        pq = []
        res = []
        for i, employee in enumerate(schedule):
            interval = employee[0]
            heappush(pq, (interval.start, i, 0))

        pre = None
        while pq:
            # pop the interval with next smallest start time
            _, employee, idx = heappop(pq)
            intv = schedule[employee][idx]

            # construct res
            if not pre:
                pre = intv
            elif pre.end < intv.start:
                res.append(Interval(pre.end, intv.start))
                pre = intv
            else:
                pre.end = max(pre.end, intv.end)

            # get the next interval from the corresponding employee if any left
            if idx < len(schedule[employee]) - 1:
                nxt_intv = schedule[employee][idx + 1]
                heappush(pq, (nxt_intv.start, employee, idx + 1))

        return res
