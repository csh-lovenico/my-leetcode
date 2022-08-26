import collections


# ac but slow
# better solution:
# https://leetcode.com/problems/maximum-frequency-stack/discuss/2443908/67-Tc-and-76-Sc-easy-python-solution
class FreqStack:

    def __init__(self):
        self.max_value = -1
        self.freq_table = collections.defaultdict(list)
        self.num_table = collections.defaultdict(int)

    def push(self, val: int) -> None:
        prev_num = self.num_table[val]
        self.num_table[val] += 1
        self.freq_table[prev_num + 1].append(val)
        self.max_value = max(self.max_value, prev_num + 1)

    def pop(self) -> int:
        # old approach: get the last element of the dict and delete if empty -- very slow!
        # solution: use a variable to track current max value
        val = self.freq_table[self.max_value].pop()
        self.num_table[val] -= 1
        if len(self.freq_table[self.max_value]) == 0:
            self.max_value -= 1
        return val
