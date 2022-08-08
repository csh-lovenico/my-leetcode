# The isBadVersion API is already defined for you.
import math


def isBadVersion(version: int) -> bool:
    return version >= 9


class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        lower = 1
        upper = n
        mid = 1
        if isBadVersion(lower):
            return lower
        # binary search
        while lower < upper:
            mid = math.ceil((upper + lower + 1) / 2)
            if isBadVersion(mid):
                upper = mid - 1
            if not isBadVersion(mid):
                lower = mid
        # handle when bad version is odd
        if not isBadVersion(mid):
            return mid + 1
        else:
            return mid


if __name__ == '__main__':
    print(Solution().firstBadVersion(11))
