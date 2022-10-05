from typing import List


# https://leetcode.com/problems/increasing-triplet-subsequence/discuss/1421787/Simple-Python-greedy-solution-3-cases
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = min2 = float("inf")
        # scan once to find min1 < min2 < n
        for i, n in enumerate(nums):
            if min1 < min2 < n:
                return True
            elif n < min1:
                min1 = n
            elif min1 < n < min2:
                min2 = n
        return False
