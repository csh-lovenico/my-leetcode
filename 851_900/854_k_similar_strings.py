# https://leetcode.com/problems/k-similar-strings/discuss/265752/Optimized-backtracking-in-Python-44-ms-faster-than-97.24
# DFS with backtracking
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        n, b = len(s1), list(s2)
        min_step = float('inf')

        def backtracking(step, i):
            nonlocal min_step
            if step >= min_step:  # exceed min_step, early stop
                return

            while i < n and s1[i] == b[i]:
                i += 1

            if i == n:
                min_step = min(step, min_step)
                return

            pos = []
            for j in range(i + 1, n):
                if b[j] == s1[i]:
                    # should be the optimal swap, match two pairs in one swap,
                    # even if have multiple A[j]==b[i], we can just pick any one
                    if s1[j] == b[i]:
                        pos = [j]
                        break
                    elif s1[j] != b[j]:  # if A[j] == b[j], this swap also remain one mis-match, exclude this situation
                        pos.append(j)

            for k in pos:
                b[i], b[k] = b[k], b[i]
                backtracking(step + 1, i)
                b[i], b[k] = b[k], b[i]

        backtracking(0, 0)
        return min_step


# DFS
class SolutionDFS:
    # DFS
    def kSimilarity(self, A: str, B: str) -> int:
        N = len(A)

        def dfs(A, B, pos):
            # pos: current index to be compared
            if A == B:
                return 0

            while A[pos] == B[pos]:
                pos += 1

            # pos: current index that A is different from B

            minCnt = float('inf')
            for i in range(pos + 1, N):
                # indexes before pos are finished, so start searching from pos + 1
                if B[i] == A[pos] and B[i] != A[i]:
                    # find a match and swap
                    B[i], B[pos] = B[pos], B[i]

                    tmp = dfs(A, B, pos + 1) + 1
                    minCnt = min(tmp, minCnt)
                    B[i], B[pos] = B[pos], B[i]

            return minCnt

        return dfs(list(A), list(B), 0)