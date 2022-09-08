class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        left = 0
        match = 0
        while left + match < len(haystack):
            if haystack[left + match] != needle[match]:
                left += 1
                match = 0
            else:
                match += 1
            if match == len(needle):
                return left
        return -1
