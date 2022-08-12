from typing import List


# https://leetcode.com/problems/combination-sum/discuss/2401526/Python-Easy-to-Understand-Sol.-using-Backtracking
class Solution:
    def __init__(self):
        self.result = []
        self.target = None
        self.candidates = None

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.target = target
        self.candidates = candidates
        # use dfs to add up the numbers
        self.dfs(0, [])
        return self.result

    def dfs(self, index: int, stack: List):
        if sum(stack) == self.target:
            self.result.append(stack.copy())
            return

        if sum(stack) > self.target:
            return

        for i in range(index, len(self.candidates)):
            stack.append(self.candidates[i])
            self.dfs(i, stack)
            stack.pop()


if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 6, 7], 7))
