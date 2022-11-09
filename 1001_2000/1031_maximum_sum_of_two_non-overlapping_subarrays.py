from typing import List


# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/discuss/1621533/Python-simple-or-time-O(n)-space-O(1)or-84.06
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        # We don't really need to deepcopy here, we can use A instead of nums.
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]  # nums value at index i is the total sum from beginning to index i
        # initializing the variables
        lmax, mmax, res = 0, 0, 0
        nums.insert(0, 0)
        # adding a dummy 0 value at the beginning of the list to make boundary coding simpler
        # L: first, M: second

        # L before M. We keep on moving the M sized window and for each position check the max sum valued L window
        # till now and update the total value for each move
        for i in range(firstLen + 1,
                       len(nums) - secondLen + 1):
            # check the boundaries by drawing array diag on paper with some example
            msum = nums[i + secondLen - 1] - nums[i - 1]
            lmax = max(lmax, nums[i - 1] - nums[i - 1 - firstLen])
            res = max(res, msum + lmax)
        # M before L. We keep on moving L sized window at each step and calculate the max sum val of M sized windows
        # lying before it.and update the total value for each move

        for i in range(secondLen + 1,
                       len(nums) - firstLen + 1):
            # check the boundaries by drawing array diag on paper with some example
            lsum = nums[i + firstLen - 1] - nums[i - 1]
            mmax = max(mmax, nums[i - 1] - nums[i - 1 - secondLen])
            res = max(res, lsum + mmax)
        return res
