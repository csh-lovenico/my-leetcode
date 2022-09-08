from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        for i in range(len(digits) - 1, -1, -1):
            if carry:
                digits[i] += 1
                carry = False
            if digits[i] >= 10:
                digits[i] %= 10
                carry = True
        if carry:
            return [1] + digits.copy()
        else:
            return digits.copy()
