from typing import List


# https://leetcode.com/problems/missing-ranges/discuss/2518405/Python-easy-solution-greater-Time%3A-O(n)-Space%3A-O(n)
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:

        def stringify(a, b):
            if a == b:
                return str(a)
            return str(a) + "->" + str(b)

        nums = [lower - 1] + nums + [upper + 1]  # Avoid to having to handle edge cases
        res = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                res.append(stringify(nums[i - 1] + 1, nums[i] - 1))
        return res
    # Time: O(n) where n is the length of nums. Creating the strings is O(1) time
    #         because nums[i] is at most 100, which means it has maximum three digits
    # Space: O(n) for the res list


if __name__ == '__main__':
    print(Solution().findMissingRanges([], 1, 1))
