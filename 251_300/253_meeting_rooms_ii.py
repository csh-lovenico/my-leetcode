import heapq
from typing import List


# https://leetcode.com/problems/meeting-rooms-ii/discuss/2441618/Python-runtime-24.39-memory-83.79
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sort by beginning time of conf room
        # for loop to store the end time in min heap
        # if the end time > start time of new interval, push in heap
        # update to the end time

        intervals.sort(key=lambda x: x[0])
        heap = [intervals[0][1]]
        heapq.heapify(heap)
        for interval in intervals[1:]:
            if interval[0] >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, interval[1])
        return len(heap)
