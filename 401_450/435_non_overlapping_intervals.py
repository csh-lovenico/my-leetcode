from typing import List


# https://leetcode.com/problems/non-overlapping-intervals/discuss/2449628/Easy-to-understand-python-solution-(97.9-faster)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        # choose as many intervals as possible
        count = 1
        ps, pe = intervals[0]  # previous start and previous finish
        for s, e in intervals:
            if s < pe:
                continue
            else:
                ps, pe = s, e
                count += 1
        return len(intervals) - count
