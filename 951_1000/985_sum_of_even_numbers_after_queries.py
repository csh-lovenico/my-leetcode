from typing import List


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        s = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                s += nums[i]
        for add, idx in queries:
            curr = nums[idx]
            if curr % 2 == 0:
                nums[idx] += add
                if nums[idx] % 2 == 0:
                    s += add
                else:
                    s -= curr
            else:
                nums[idx] += add
                if nums[idx] % 2 == 0:
                    s += nums[idx]
            res.append(s)
        return res
