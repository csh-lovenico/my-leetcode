# https://leetcode.com/problems/divide-two-integers/discuss/2508636/Divide-Two-Integers-or-Easy-and-understandable-code-or-Python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        # Storing sign if any one is negative
        if (dividend < 0) ^ (divisor < 0):
            sign = -1

        dividend = abs(dividend)
        divisor = abs(divisor)
        temp = quotient = 0
        for i in range(31, -1, -1):
            if temp + (divisor << i) <= dividend:
                temp += divisor << i
                quotient += 1 << i
        if sign == -1:
            quotient = -quotient
        # handling if goes out of range i.e (2**(31))-1
        if abs(quotient) > (1 << 31 - 1) and quotient > 0:
            quotient = (1 << 31) - 1
        return quotient
