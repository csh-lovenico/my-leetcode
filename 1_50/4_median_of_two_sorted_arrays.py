import heapq
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # min stack: stores the second half of the all numbers
        min_stack = []
        # max stack: stores first half of the all numbers
        max_stack = []
        all_num = nums1 + nums2
        for num in all_num:
            heapq.heappush(max_stack, -1 * num)
            if min_stack and max_stack and max_stack[0] * -1 > min_stack[0]:
                val = heapq.heappop(max_stack) * -1
                heapq.heappush(min_stack, val)
            if len(max_stack) > len(min_stack):
                val = heapq.heappop(max_stack) * -1
                heapq.heappush(min_stack, val)
            if len(min_stack) > len(max_stack):
                val = heapq.heappop(min_stack) * -1
                heapq.heappush(max_stack, val)

        if len(max_stack) > len(min_stack):
            return max_stack[0] * -1
        if len(min_stack) > len(max_stack):
            return min_stack[0]
        return (min_stack[0] + max_stack[0] * -1) / 2


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1, 3], [2]))
