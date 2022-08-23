from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        num_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        stack1: List[str] = []
        stack2: List[str] = []
        stack1.extend(num_dict[digits[0]])
        for i in range(1, len(digits)):
            if len(stack1) == 0:
                while stack2:
                    current_string = stack2.pop()
                    for letter in num_dict[digits[i]]:
                        new_string_cp = current_string
                        new_string_cp += letter
                        stack1.append(new_string_cp)
            else:
                while stack1:
                    current_string = stack1.pop()
                    for letter in num_dict[digits[i]]:
                        new_string_cp = current_string
                        new_string_cp += letter
                        stack2.append(new_string_cp)

        if stack1:
            return stack1
        else:
            return stack2
