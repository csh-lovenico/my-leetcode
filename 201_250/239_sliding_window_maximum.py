from collections import deque
from typing import List


# https://leetcode.com/problems/sliding-window-maximum/discuss/2484057/Simple-Python-Monotonic-Queue-O(N)-Solution
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Keep track of maximum elements with queue
        # (monotonically increasing queue - elems on front > elems on back)
        mono_queue = deque()

        # An array for final max elements and a left pointer
        max_elems = []
        left = 0

        # Go through all elements with right pointer
        for right in range(len(nums)):
            # Pop front elem if it's lower than left side of the window (out of range)
            while mono_queue and mono_queue[0] < left:
                mono_queue.popleft()

            # Keep popping right elems that are smaller/equal to current element
            while mono_queue and nums[right] >= nums[mono_queue[-1]]:
                mono_queue.pop()

            # Append current elem to the correct position in queue
            mono_queue.append(right)

            print(mono_queue)
            # If we are in a window
            if right >= k - 1:
                # Append max elem from queue (front of queue) & increment left of window
                max_elems.append(nums[mono_queue[0]])
                left += 1

        return max_elems


if __name__ == '__main__':
    print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
