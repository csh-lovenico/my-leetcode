from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = dict()
        for i in range(len(strs)):
            key = ''.join(sorted(list(strs[i])))
            val = ana_dict.get(key, [])
            val.append(strs[i])
            ana_dict[key] = val

        result = []
        for _, v in ana_dict.items():
            result.append(v)

        return result
