from typing import List


# https://leetcode.com/problems/optimal-division/solutions/101691/easy-python-solution-with-interpretation/
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        # make the parenthesis begin from the second number and end after the last number
        # get the largest numerator and the smallest denominator
        if len(nums) < 3:
            result = ''.join([str(num) + '/' for num in nums])
            return result[:-1]
        result = []
        result.append(str(nums[0]) + '/(')
        for i in range(1, len(nums)):
            result.append(str(nums[i]))
            result.append('/')
        result = result[:-1]
        result.append(')')
        return ''.join(result)
