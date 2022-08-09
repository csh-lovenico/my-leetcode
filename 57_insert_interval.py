from typing import List


# Not my original solution. Comments are added by me.
# https://leetcode.com/problems/insert-interval/discuss/2397159/python-or-easy-or-O(n)-or-readable-or-beginner-friendly
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # insert the new interval to the right place
        insert_point = self.find_insert_point(intervals, newInterval)
        if insert_point == len(intervals):
            intervals.append(newInterval)
        else:
            intervals.insert(insert_point, newInterval)
        # use a new list to save the answer
        result = [intervals[0]]
        prev = result[0]

        for i in range(1, len(intervals)):
            curr = intervals[i]
            # if the current interval overlaps the previous interval
            # merge the two intervals and add the new one to the answer list
            if self.check_overlap(prev, curr):
                result.pop()
                result.append([min(prev[0], curr[0]), max(prev[1], curr[1])])
                # set previous interval to the last element in the answer list
                # which is the new interval
                prev = result[-1]

            # current interval does not overlap the previous interval
            else:
                # if the current interval is completely in the previous interval
                # ignore this interval
                if prev[0] <= curr[0] and prev[1] >= curr[1]:
                    continue

                # append current interval and move to next
                result.append(curr)
                prev = curr
        return result

    def find_insert_point(self, intervals: List[List[int]], newInterval: List[int]) -> int:
        for i in range(len(intervals)):
            if intervals[i][0] >= newInterval[0]:
                return i
        return len(intervals)

    def check_overlap(self, prev, curr):
        # checks if the end of the previous interval lies between the current interval
        if curr[0] <= prev[1] <= curr[1]:
            return True
        else:
            return False
