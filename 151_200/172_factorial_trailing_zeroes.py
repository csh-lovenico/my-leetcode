

# https://leetcode.com/problems/factorial-trailing-zeroes/discuss/2497807/Python-solution-with-explanations.
class Solution:
    def trailingZeroes(self, n: int) -> int:
        # divisor like 5, 10, 15, multiple of 5, has only one '5' factor

        # divisor like, 25, 50, 75, multiple of 25, has additional '5' factor

        # divisor like 125, 250, 375, multiple of 125 ( 5*5*5) has additional '5' factor

        # total # of '5' factor is the number of '0' in n! since only 2 * 5 can result a 10

        divisor = 5

        res = 0

        while divisor <= n:
            res += n // divisor
            divisor *= 5

        return res
