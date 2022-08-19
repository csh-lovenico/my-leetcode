from typing import List


# https://leetcode.com/problems/longest-consecutive-sequence/discuss/2429349/Python-Hash-Table-and-Intelligent-Sequence-Building-Solution-or-O(n)-Time-or-O(n)-Space
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_sequence = 0
        for num in nums:
            # * Check if it's the start of a sequence
            # * Start of the sequence wouldn't have any left neighbors
            if (num-1) not in nums_set:
                cur_sequence = 1
                while (num+cur_sequence) in nums_set:
                    cur_sequence += 1

                longest_sequence = max(longest_sequence, cur_sequence)

        return longest_sequence