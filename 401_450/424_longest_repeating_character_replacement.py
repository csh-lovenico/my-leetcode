# https://leetcode.com/problems/longest-repeating-character-replacement/discuss/2433943/PYTHON-SLIDING-WINDOW-EASY-COMMENTED
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}  # dictionary to maintain frequency
        i, j = 0, 0  # iterators for getting size of window
        maxlen = 0  # will be  our answer

        while j < len(s):
            # first taking the frequency in the dictionary
            if s[j] not in d:
                d[s[j]] = 1
            else:
                d[s[j]] += 1

            l = j - i + 1  # len of the window
            # l - max(d.values()) is the number of unique chars
            if l - max(d.values()) > k:  # if unique charecters > k
                d[s[i]] -= 1
                # will be shifting our left pointer to decrease the size of window to adjust sum of
                # unique chars and same chars.
                if d[s[i]] == 0:
                    del d[s[i]]
                i += 1
            else:
                maxlen = max(l, maxlen)  # updating the answer if all conditions are satisfied
            j += 1
        return maxlen
