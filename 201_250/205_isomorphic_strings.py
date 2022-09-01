import collections


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp = {}
        visited = set()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in mp:
                if t[i] in visited:
                    return False
                mp[s[i]] = t[i]
                visited.add(t[i])
            else:
                if mp[s[i]] != t[i]:
                    return False
        return True
