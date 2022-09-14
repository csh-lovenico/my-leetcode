from typing import List


# brute-force, O(n^2), TLE
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        def ck(interval_1: List[int], interval_2: List[int]):
            return interval_1[0] <= interval_2[0] <= interval_1[1]

        intervals.sort()
        curr = intervals[0].copy()
        upper = curr[1]
        idx = 0
        result = 0
        visited = [False] * len(intervals)
        visited[0] = True
        while True:
            for i in range(idx, len(intervals)):
                if not visited[i] and not ck([curr[0], upper], intervals[i]):
                    visited[i] = True
                    upper = intervals[i][1]
            curr = None
            for j in range(idx, len(visited)):
                if not visited[j]:
                    idx = j
                    curr = intervals[j].copy()
                    visited[j] = True
                    upper = curr[1]
                    break
            result += 1
            if curr is None:
                break
        return result

# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/discuss/2560101/JavaC%2B%2BPython-Meeting-Room
    def minGroupsOptimized(self, intervals: List[List[int]]) -> int:
        A = []
        for a, b in intervals:
            A.append([a, 1])
            A.append([b + 1, -1])
        res = cur = 0
        print(sorted(A))
        for a, diff in sorted(A):
            cur += diff
            res = max(res, cur)
            print(res)
        return res


if __name__ == '__main__':
    print(Solution().minGroupsOptimized(
        [[441459, 446342], [801308, 840640], [871890, 963447], [228525, 336985], [807945, 946787], [479815, 507766],
         [693292, 944029], [751962, 821744]]))
