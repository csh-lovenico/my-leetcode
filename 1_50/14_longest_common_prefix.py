import math
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = math.inf
        result_list = []
        for i in range(len(strs)):
            min_length = min(min_length, len(strs[i]))

        for i in range(min_length):
            is_same = True
            for j in range(1, len(strs)):
                if strs[j - 1][i] != strs[j][i]:
                    is_same = False
            if is_same:
                result_list.append(strs[0][i])
                continue
            else:
                break

        return ''.join(result_list)
