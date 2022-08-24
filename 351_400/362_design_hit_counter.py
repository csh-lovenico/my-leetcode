import collections


class HitCounter:

    def __init__(self):
        self.hit_dict = collections.defaultdict(int)

    def hit(self, timestamp: int) -> None:
        self.hit_dict[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        return sum(self.hit_dict[i] for i in range(timestamp, timestamp - 300, -1))
