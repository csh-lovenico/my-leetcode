from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        hashmap = {}
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = i

        print(hashmap)

        for i in range(len(distance)):
            char = chr(ord('a') + i)
            if chr not in hashmap:
                continue
            idx = hashmap[char]
            if idx + distance[i] + 1 >= len(s):
                return False
            elif s[idx + distance[i] + 1] != s[idx]:
                return False
            else:
                continue

        return True
