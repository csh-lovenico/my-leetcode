# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

pick = 10


# the problem does not include the implementation of this function
def guess(num: int) -> int:
    if num < pick:
        return 1
    elif num > pick:
        return -1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        low = 0
        high = n
        mid = (low + high + 1) // 2
        res = guess(mid)
        while res != 0:
            if res == 1:
                low = mid
            elif res == -1:
                high = mid
            mid = (high + low + 1) // 2
            res = guess(mid)
            print(mid)
        return mid


if __name__ == '__main__':
    print(Solution().guessNumber(10))
