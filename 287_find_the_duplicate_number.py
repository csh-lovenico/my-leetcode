from typing import List


# https://leetcode.com/problems/find-the-duplicate-number/discuss/2426143/Python-O(n)-solution-linear-time-constant-space-and-no-modifications-to-array
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd Warshall Algorithm
        # similar to check if linked list has cycle and locate the start of the cycle
        slow, fast = 0, 0  # 0 is not a part of the cycle
        while True:
            slow = nums[slow]  # equivalent to slow.next in linked list
            fast = nums[nums[fast]]  # equivalent to fast.next.next in linked list
            if slow == fast:
                break

        slow2 = 0
        # Currently, slow is at the intersection of the slow and fast pointers, which is
        # always going to be the same distance from the start of the cycle as slow 2
        while True:
            slow = nums[slow]  # equivalent to slow.next in linked list
            slow2 = nums[slow2]  # equivalent to slow2.next in linked list
            if slow == slow2:  # will always intersect at the start of the cycle
                return slow
