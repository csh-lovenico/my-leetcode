from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image
        queue = [[sr, sc]]
        while len(queue) > 0:
            head = queue.pop(0)
            if image[head[0]][head[1]] == original_color:
                image[head[0]][head[1]] = color
            else:
                continue
            if head[0] > 0:
                queue.append([head[0] - 1, head[1]])
            if head[1] > 0:
                queue.append([head[0], head[1] - 1])
            if head[0] < len(image) - 1:
                queue.append([head[0] + 1, head[1]])
            if head[1] < len(image[0]) - 1:
                queue.append([head[0], head[1] + 1])
        return image
