from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # if using brute-force:
        # calculate all combinations of intervals that will not overlap each other and add up profits
        # below is a dp solution
        n = len(profit)
        jobs = [(startTime[i], endTime[i], profit[i]) for i in range(n)]
        jobs.sort(key=lambda x: x[1])

        def binarySearch(x, low, high):

            while low <= high:
                mid = (low + high) // 2
                if jobs[mid][1] <= x:
                    low = mid + 1
                else:
                    high = mid - 1

            return high

        total_profit = [0] * n
        for index in range(n):
            i = binarySearch(jobs[index][0], 0, index - 1)
            to_add = total_profit[i] if i != -1 else 0
            total_profit[index] = max(total_profit[index - 1], jobs[index][2] + to_add)

        return total_profit[-1]
