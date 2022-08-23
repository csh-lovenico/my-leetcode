from typing import List


# https://leetcode.com/problems/single-number/discuss/2402233/Using-Bit-Manipulation-(-XOR-)-greater-PythonSolution
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0  # initialized to zero , because XOR of any number with 0 is 0.
        for num in nums:
            res = res ^ num
        return res
