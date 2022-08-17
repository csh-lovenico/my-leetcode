from typing import List


# https://leetcode.com/problems/gas-station/discuss/2395794/Python-Very-Simple-O(n)-Solution-with-Explanation
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        cur_gas = 0
        # if run out of gas on the way to the next station, just start from the next station
        for i in range(len(gas)):
            cur_gas += gas[i] - cost[i]
            if cur_gas < 0:
                start = i + 1
                cur_gas = 0

        return start
