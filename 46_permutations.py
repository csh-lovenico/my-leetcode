from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(stack: List[int], num_list: List[int]):
            if len(num_list) == 0:
                result.append(stack.copy())
                return
            for i in range(len(num_list)):
                new_stack = stack.copy()
                new_stack.append(num_list[i])
                next_list = num_list.copy()
                next_list.remove(num_list[i])
                dfs(new_stack, next_list)
        dfs([], nums)
        return result
