import collections
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        p_dict = collections.defaultdict(lambda: 0)
        s_dict = collections.defaultdict(lambda: 0)
        result = []
        for i in range(len(p)):
            p_dict[p[i]] += 1
        for i in range(len(p)):
            s_dict[s[i]] += 1
        current_start = 0
        current_end = len(p) - 1
        while current_end < len(s) - 1:
            is_same = True
            for k, v in p_dict.items():
                if s_dict[k] != v:
                    is_same = False
                    break
            if is_same:
                result.append(current_start)
            current_start += 1
            current_end += 1
            s_dict[s[current_start - 1]] -= 1
            s_dict[s[current_end]] += 1

        is_same = True
        for k, v in p_dict.items():
            if s_dict[k] != v:
                is_same = False
                break
        if is_same:
            result.append(current_start)
        return result


if __name__ == '__main__':
    print(Solution().findAnagrams("abab", "ab"))
