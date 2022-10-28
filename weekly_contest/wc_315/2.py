from typing import List


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        def reverse(n: int) -> int:
            if 1 <= n < 10:
                return n
            res = 0
            while n > 0:
                res *= 10
                res += n % 10
                n = n // 10
            return res

        s = set(nums)
        for i in range(len(nums)):
            s.add(reverse(nums[i]))
        return len(s)
