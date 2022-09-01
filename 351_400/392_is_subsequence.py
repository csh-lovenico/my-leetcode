class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        elif t == "":
            return False
        match = 0
        for i in range(len(t)):
            if s[match] == t[i]:
                match += 1
                if match == len(s):
                    return True
        return False
