from typing import List


# bit manipulation
# https://leetcode.com/problems/subsets/discuss/2405915/Python-simple-Solution-using-Bit-manipulation-and-Backtracking-%2B-Recursion
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        total_sets = 2 ** n
        ans = []
        # use 000...0 - 111...1 to represent each case
        for i in range(0, total_sets):
            temp = []
            temp_binary = bin(i)
            temp_binary = list(temp_binary[2:])
            temp_binary.reverse()
            for j in range(0, len(temp_binary)):
                if temp_binary[j] == '1':
                    temp.append(nums[j])
            ans.append(temp)
        return ans
