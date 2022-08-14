import math


# https://leetcode.com/problems/minimum-window-substring/discuss/2406086/Commented-Sliding-window-approach-python-using-hashmaps%3A
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        map_t, map_s = {}, {}
        left_ptr = 0
        matched = 0
        min_length = math.inf

        res = [-1, -1]

        for i in range(len(t)):
            map_t[t[i]] = map_t.get(t[i], 0) + 1

        for r in range(len(s)):
            map_s[s[r]] = map_s.get(s[r], 0) + 1

            if s[r] in map_t and map_t[s[r]] == map_s[s[r]]:
                matched += 1

            while matched == len(map_t):
                if r - left_ptr + 1 < min_length:
                    res = [left_ptr, r]
                    min_length = r - left_ptr + 1
                map_s[s[left_ptr]] -= 1

                if s[left_ptr] in map_t and map_s[s[left_ptr]] < map_t[s[left_ptr]]:
                    matched -= 1
                left_ptr += 1

        left_ptr, right_ptr = res
        return s[left_ptr:right_ptr + 1] if min_length != math.inf else ""
