from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        result = []
        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                stack.append(asteroids[i])
            else:
                if not stack:
                    result.append(asteroids[i])
                else:
                    while stack and stack[-1] < abs(asteroids[i]):
                        stack.pop()
                    if not stack:
                        result.append(asteroids[i])
                        continue
                    else:
                        if stack[-1] == abs(asteroids[i]):
                            stack.pop()
                            continue
                        elif stack[-1] > abs(asteroids[i]):
                            continue
        result.extend(stack)
        return result
