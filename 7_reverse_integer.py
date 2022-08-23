class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x = -x

        result = 0
        while x:
            left = x % 10
            result = result * 10 + left
            x = x // 10
            if not (-2 ** 31 <= result <= (2 ** 31 - 1)):
                return 0
        if negative:
            return -result
        else:
            return result
