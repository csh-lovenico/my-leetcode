import math


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        lst = float('inf')
        while n > 0:
            max_log = math.floor(math.log10(n) / math.log10(3))
            # use math.log(n, 3) may get inaccurate answer
            # log(243, 3) = 4.9999999999
            # math.log(n, 3) == math.log10(n) / math.log10(3)
            if lst == max_log:
                return False
            else:
                lst = max_log
                n -= 3 ** max_log

        return True
