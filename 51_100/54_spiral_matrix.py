from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        result = []
        max_x = len(matrix) - 1
        max_y = len(matrix[0]) - 1

        def spiral_visit(x: int, y: int, direction: str):
            result.append(matrix[x][y])
            matrix[x][y] = -101
            if direction == "right":
                if y < max_y and matrix[x][y + 1] != -101:
                    spiral_visit(x, y + 1, "right")
                else:
                    if x < max_x and matrix[x + 1][y] != -101:
                        spiral_visit(x + 1, y, "down")
                    else:
                        return
            if direction == "down":
                if x < max_x and matrix[x + 1][y] != -101:
                    spiral_visit(x + 1, y, "down")
                else:
                    if y > 0 and matrix[x][y - 1] != -101:
                        spiral_visit(x, y - 1, "left")
                    else:
                        return
            if direction == "left":
                if y > 0 and matrix[x][y - 1] != -101:
                    spiral_visit(x, y - 1, "left")
                else:
                    if x > 0 and matrix[x - 1][y] != -101:
                        spiral_visit(x - 1, y, "up")
                    else:
                        return
            if direction == "up":
                if x > 0 and matrix[x - 1][y] != -101:
                    spiral_visit(x - 1, y, "up")
                else:
                    if y < max_y and matrix[x][y + 1] != -101:
                        spiral_visit(x, y + 1, "right")
                    else:
                        return

        spiral_visit(0, 0, "right")
        return result
