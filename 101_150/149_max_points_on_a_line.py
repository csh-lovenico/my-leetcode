from typing import List


# https://leetcode.com/problems/max-points-on-a-line/discuss/2600030/Easy-To-Understand-or-Max-Points-on-a-line-using-slope-formula-using-dictionary-in-easy-way
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 0
        n = len(points)
        if n <= 2:
            return n
        for i in range(n):
            d = {}
            for j in range(i + 1, n):
                if points[j][0] == points[i][0]:
                    slope = 'inf'
                else:
                    slope = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
                if slope in d:
                    d[slope] += 1
                else:
                    d[slope] = 1
                res = max(res, d[slope])
        return res + 1
