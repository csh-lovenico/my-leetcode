from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l = 0
        r = 1
        curr = colors[0]
        ans = 0
        while r <= len(colors):
            if r == len(colors):
                if r - l == 1:
                    break
                else:
                    sub = neededTime[l:r]
                    sub.sort()
                    ans += sum(sub[:-1])
                    break
            if colors[r] != curr:
                length = r - l
                if length > 1:
                    sub = neededTime[l:r]
                    sub.sort()
                    ans += sum(sub[:-1])
                l = r
                r = r + 1
                curr = colors[l]
            else:
                r = r + 1
        return ans
# optimized solution: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/discuss/2657501/99-faster-or-Python-or-O(n)-or-10-lines-or-Easy-to-understand
