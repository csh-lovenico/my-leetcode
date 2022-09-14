import collections


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s_cow = collections.defaultdict(int)
        g_cow = collections.defaultdict(int)
        b = 0
        c = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                b += 1
            else:
                s_cow[secret[i]] += 1
                g_cow[guess[i]] += 1
        for i in range(10):
            c += min(s_cow[str(i)], g_cow[str(i)])

        return str(b) + 'A' + str(c) + 'B'
