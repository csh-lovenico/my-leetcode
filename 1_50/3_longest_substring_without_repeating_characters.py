class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        # slide window
        current_start = 0
        current_end = 1
        max_length = 1
        while current_end < len(s):
            if s[current_end] not in s[current_start:current_end]:
                current_end = current_end + 1
            else:
                current_length = current_end - current_start
                if max_length < current_length:
                    max_length = current_length
                # move the start after the duplicated letter
                index = s[current_start:current_end].index(s[current_end])
                current_start = current_start + index + 1
        current_length = current_end - current_start
        if max_length < current_length:
            max_length = current_length
        return max_length
