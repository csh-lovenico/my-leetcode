import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_dict = collections.defaultdict(lambda: 0)
        for word in words:
            word_dict[word] -= 1
        heap = []
        for key, value in word_dict.items():
            heapq.heappush(heap, (value, key))
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result


if __name__ == '__main__':
    print(Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
