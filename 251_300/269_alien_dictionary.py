from collections import defaultdict, deque
from typing import List


# https://leetcode.com/problems/alien-dictionary/discuss/2362680/Topological-Sort-with-steps-explained
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        n = len(words)

        # if there is only one word, then order is unknown, return the set of letters
        if n == 1:
            return "".join(set(words[0]))

        indeps = defaultdict(int)
        children = defaultdict(list)

        # initialize all available letters
        for ltr in set("".join(words)):
            indeps[ltr] = 0

        # build the graph
        n = len(words)
        for i in range(n - 1):
            curr = words[i]
            next = words[i + 1]
            nw = min(len(curr), len(next))

            # flag for checking if any differences were detected
            flag = False

            # for each pair of consecutive words, compare each letter until a different is found
            # that difference indicates the lexicographical order relationship between those letters
            for j in range(nw):
                if curr[j] != next[j]:
                    indeps[next[j]] += 1
                    children[curr[j]].append(next[j])
                    flag = True
                    break

            # if all letters were the same; however curr word is larger than next word, then order is invalid
            if not flag and len(curr) > len(next):
                return ""

        # add letters with zero deps to the queue
        q = deque([])
        for k, v in indeps.items():
            if v == 0:
                q.append(k)

        # iteratively remove letters with zero deps from the graph
        res = ""
        while q:
            curr = q.popleft()
            res += curr
            for child in children[curr]:
                indeps[child] -= 1
                if indeps[child] == 0:
                    q.append(child)

        # if the number of letters removed does not match the number of available letters, solution is impossible
        if len(res) != len(indeps.keys()):
            return ""
        return res