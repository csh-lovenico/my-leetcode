from collections import defaultdict
from typing import List


class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        edge_score = defaultdict(lambda: 0)
        for i in range(len(edges)):
            edge_score[str(edges[i])] += i
        edge_score_list = []
        for k, v in edge_score.items():
            edge_score_list.append((v, k))
        edge_score_list.sort(reverse=True)
        max_score = edge_score_list[0][0]
        for i in range(len(edge_score_list)):
            if edge_score_list[i][0] < max_score:
                return edge_score_list[i - 1][1]
        return edge_score_list[-1][1]
