from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            result.append(bin(i).count('1'))
        return result

# another solution: https://leetcode.com/problems/counting-bits/discuss/2421797/PYTHON-All-you-need-to-do-is-duplicating-the-array-use-nothing-but-append
