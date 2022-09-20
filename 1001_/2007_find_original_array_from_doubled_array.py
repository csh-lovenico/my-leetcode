import collections
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        result = []
        changed.sort()
        hashmap = collections.Counter(changed)
        for n in changed:
            if n != 0 and hashmap[n] > 0 and hashmap[n * 2] > 0:
                result.append(n)
                hashmap[n] -= 1
                hashmap[n * 2] -= 1
            elif n == 0:
                if hashmap[n] % 2 != 0:
                    return []
                else:
                    result.extend([0] * (hashmap[n] // 2))
                    hashmap[n] = 0
        if len(result) * 2 == len(changed):
            return result
        else:
            return []

# ac but slow (using dict)
# optimized way using collections.Counter
# https://leetcode.com/problems/find-original-array-from-doubled-array/discuss/2578114/Short-oror-C%2B%2B-oror-Java-oror-PYTHON-oror-Explained-Solution-oror-Beginner-Friendly-oror-BY-MR-CODER
