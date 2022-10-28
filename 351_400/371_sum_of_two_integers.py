# (TLE in Python)
# https://leetcode.com/problems/sum-of-two-integers/discuss/2481594/How-computers-Calculate-How-add-without-using-%22%2B%22-and-%22-%22

# https://leetcode.com/problems/sum-of-two-integers/discuss/2225341/5-Interesting-Solutions-greater-Python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits integer min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)

    def getSumTle(self, a: int, b: int) -> int:
        while b:
            carry = a & b
            # a & b is the carry of a + b
            a = a ^ b
            # a ^ b is a + b without carry
            b = carry << 1
            # carry should right shift 1 bit to put on the right place
        return a
