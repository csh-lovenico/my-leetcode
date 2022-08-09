from typing import List


# accepted but slow
# using dp may be faster
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        zero_queue = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    zero_queue.append([i, j, 0])
        return self.bfs(mat, zero_queue)

    def bfs(self, mat: List[List[int]], queue: List[List[int]]) -> List[List[int]]:
        max_x = len(mat)
        max_y = len(mat[0])
        visited = [[False for i in range(max_y)] for j in range(max_x)]
        for i in range(len(queue)):
            visited[queue[i][0]][queue[i][1]] = True
        while len(queue) > 0:
            head = queue.pop(0)
            if mat[head[0]][head[1]] == 0 and visited[head[0]][head[1]] == 0:
                continue
            elif not visited[head[0]][head[1]]:
                mat[head[0]][head[1]] = head[2]
                visited[head[0]][head[1]] = True
                if head[0] > 0:
                    queue.append([head[0] - 1, head[1], head[2] + 1])
                if head[1] > 0:
                    queue.append([head[0], head[1] - 1, head[2] + 1])
                if head[0] < max_x - 1:
                    queue.append([head[0] + 1, head[1], head[2] + 1])
                if head[1] < max_y - 1:
                    queue.append([head[0], head[1] + 1, head[2] + 1])
            else:
                if mat[head[0]][head[1]] < head[2]:
                    continue
                else:
                    mat[head[0]][head[1]] = head[2]
                    if head[0] > 0:
                        queue.append([head[0] - 1, head[1], head[2] + 1])
                    if head[1] > 0:
                        queue.append([head[0], head[1] - 1, head[2] + 1])
                    if head[0] < max_x - 1:
                        queue.append([head[0] + 1, head[1], head[2] + 1])
                    if head[1] < max_y - 1:
                        queue.append([head[0], head[1] + 1, head[2] + 1])
        return mat


if __name__ == '__main__':
    print(Solution().updateMatrix(
        [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1],
         [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [0, 0, 0]]))
