import string
from typing import List


# https://leetcode.com/problems/word-ladder/discuss/2424791/Python-97-BFS-Brutal-force-and-optimized-bidirectional-BFS-or-Explantion-_
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # Bidirectional BFS
        # search both from the beginning and end, it has a solution if they meet at the same word
        wordDict = set(wordList)
        if endWord not in wordDict: return 0  # impossible to find a route

        wlen = len(beginWord)
        s1 = {beginWord}  # s1 starts from the front
        s2 = {endWord}  # s2 starts from the back
        step = 0

        wordDict.remove(endWord)

        while len(s1) > 0 and len(s2) > 0:
            step += 1

            # swap s1 and s2 if s2 is shorter
            if len(s1) > len(s2):
                s1, s2 = s2, s1

            s = set()
            for w in s1:
                new_words = []
                new_words = [w[:i] + t + w[i + 1:] for t in string.ascii_lowercase for i in range(wlen)]

                for new_word in new_words:

                    if new_word in s2: return step + 1  # front and back BFS meet
                    if new_word not in wordDict: continue

                    # remove it from dictionary,
                    # so we won't go through the same word twice
                    wordDict.remove(new_word)
                    s.add(new_word)
            s1 = s

        return 0
