class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start_bit = bin(start)[2:]
        goal_bit = bin(goal)[2:]

        diff = abs(len(start_bit) - len(goal_bit))

        res = 0

        if len(start_bit) < len(goal_bit):
            start_bit = "0" * diff + start_bit
        else:
            goal_bit = "0" * diff + goal_bit

        for i in range(len(start_bit)):
            if start_bit[i] != goal_bit[i]:
                res += 1

        return res
