from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
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

    def check_overlap(self, prev, curr):
        # checks if the end of the previous interval lies between the current interval
        if curr[0] <= prev[1] <= curr[1]:
            return True
        else:
            return False


if __name__ == '__main__':
    arr = [[1, 4], [0, 1]]
    arr.sort()
    print(arr)
