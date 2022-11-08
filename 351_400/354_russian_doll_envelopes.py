from typing import List


# https://leetcode.com/problems/russian-doll-envelopes/discuss/2071477/C%2B%2BJava-PythonBest-Explanation-with-Pictures
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        # LIS = the longest increasing subsequence
        LIS = []
        size = 0
        # the LIS uses binary search idea:
        # https://leetcode.com/problems/longest-increasing-subsequence/discuss/2395570/Python3-oror-7-lines-binSearch-cheating-wexplanation-oror-TM%3A-9482
        # https://leetcode.com/problems/longest-increasing-subsequence/discuss/2395661/Python-99.65-clear-explanation-or-binary-search-easy-or-simple-approach-_
        for (w, h) in envelopes:
            if not LIS or h > LIS[-1]:
                LIS.append(h)
                size += 1
            # find the smallest element larger than h in LIS and set to h
            else:
                l, r = 0, size
                while l < r:
                    m = l + (r - l) // 2
                    if LIS[m] < h:
                        l = m + 1
                    else:
                        r = m
                LIS[l] = h
        return size
