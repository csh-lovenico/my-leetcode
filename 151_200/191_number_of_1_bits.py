class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

# standard solution: https://leetcode.com/problems/number-of-1-bits/discuss/2424173/Python-Simple-and-Easy-to-Understand-Solution.
