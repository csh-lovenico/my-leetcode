import collections
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res = 0

        def isPalindrome(s: str) -> bool:
            return s[0] == s[1]

        def reverse(s: str) -> str:
            return ''.join([s[1], s[0]])

        hashmap = collections.defaultdict(int)
        # record the occurrence of each word
        for w in words:
            hashmap[w] += 1

        # for each word, find the occurrence of its reversed
        for k, v in hashmap.items():
            if hashmap[k] != 0:
                if reverse(k) in hashmap and hashmap[reverse(k)] != 0:
                    # itself is not pal,
                    if not isPalindrome(k):
                        min_val = min(hashmap[k], hashmap[reverse(k)])
                        res += 4 * min_val
                        hashmap[k] -= min_val
                        hashmap[reverse(k)] -= min_val
                    else:
                        if hashmap[k] > 1:
                            if hashmap[k] % 2 == 0:
                                res += 4 * (hashmap[k] // 2)
                                hashmap[k] = 0
                            else:
                                res += 4 * (hashmap[k] // 2)
                                hashmap[k] = 1

        for k, v in hashmap.items():
            if isPalindrome(k) and hashmap[k] == 1:
                res += 2
                break
        return res
