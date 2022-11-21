from typing import List


# https://leetcode.com/problems/longest-uncommon-subsequence-ii/solutions/1428753/python-o-n-2k-solution-explained/
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubsequence(s, t):
            t = iter(t)
            return all(c in t for c in s)

        strs.sort(key=lambda x: -len(x))
        for i, word in enumerate(strs):
            if all(not isSubsequence(word, strs[j]) for j in range(len(strs)) if j != i):
                return len(word)

        return -1
