from functools import cmp_to_key
from typing import List


# https://leetcode.com/problems/largest-number/discuss/2406725/Using-Sort-Comparator-Function-2-Solutions
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        isAllZeroes = True
        nums = [str(x) for x in nums]

        for i in nums:
            if i != '0':
                isAllZeroes = False
                break
        if isAllZeroes:
            return "0"

        nums.sort(key=cmp_to_key(self.customComparator))
        return "".join(nums)

    def customComparator(self, a, b):
        a = str(a)
        b = str(b)
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        else:
            return 0


if __name__ == '__main__':
    print(Solution().largestNumber([10, 2]))
