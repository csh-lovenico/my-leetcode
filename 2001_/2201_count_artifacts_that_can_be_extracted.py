from typing import List, Tuple


class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        grid = [[-1] * n for _ in range(n)]
        hashmap = dict()
        ans = 0

        def calcArea(artifact: List[int]) -> int:
            left_top = (artifact[0], artifact[1])
            right_bottom = (artifact[2], artifact[3])

            return (right_bottom[0] - left_top[0] + 1) * (right_bottom[1] - left_top[1] + 1)

        def calcCoordinate(artifact: List[int]) -> List[Tuple[int, int]]:
            left_top = (artifact[0], artifact[1])
            right_bottom = (artifact[2], artifact[3])
            if calcArea(artifact) == 1:
                return [left_top]
            else:
                if left_top[0] == right_bottom[0]:
                    return [(left_top[0], y) for y in range(left_top[1], right_bottom[1] + 1)]
                elif left_top[1] == right_bottom[1]:
                    return [(x, left_top[1]) for x in range(left_top[0], right_bottom[0] + 1)]
                else:
                    return [left_top, right_bottom, (left_top[0], right_bottom[1]), (right_bottom[0], left_top[1])]

        for i in range(len(artifacts)):
            hashmap[i] = calcArea(artifacts[i])
            for c in calcCoordinate(artifacts[i]):
                grid[c[0]][c[1]] = i

        for d in dig:
            curr_result = grid[d[0]][d[1]]
            if curr_result == -1:
                continue
            else:
                hashmap[curr_result] -= 1
                if hashmap[curr_result] == 0:
                    ans += 1

        return ans

    # optimized solution
    # https://leetcode.com/problems/count-artifacts-that-can-be-extracted/solutions/1844361/python-elegant-short-and-simple-to-understand-with-explanations/
    def digArtifactsOptimized(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        # record dig places and check if all the grids in artifact is in dig places
        result, dig_pos = 0, set(tuple(pos) for pos in dig)
        for pos in artifacts:
            if all((x, y) in dig_pos for x in range(pos[0], pos[2] + 1) for y in range(pos[1], pos[3] + 1)):
                result += 1
        return result
