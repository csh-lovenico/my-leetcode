from typing import List


# https://leetcode.com/problems/earliest-possible-day-of-full-bloom/discuss/2756770/Python-real-world-simple-explanation
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        prevPlant, ans = 0, 0
        # the total days needed to plant all the plants will not change
        # so make growTime of the last plant as small as possible
        # sort by grow time in descending order
        # the possible time is the growTime + plantTime of current plant + sum of plant time of prev plants
        for grow, plant in sorted(zip(growTime, plantTime), reverse=True):
            ans = max(ans, (grow + plant + prevPlant))
            prevPlant += plant
        return ans
