import math
from typing import List


class TimeMap:

    def __init__(self):
        # dict: key: key, value: timestamp -- value, timestamp_list: list[int]
        """
        'foo': { 'values':['bar',...],
        'timestamp_list':[1]
        }
        """
        self.kv = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        try:
            # position = self.find_insertion_point(self.kv[key]['timestamp_list'], timestamp)
            self.kv[key]['values'].append(value)
            self.kv[key]['timestamp_list'].append(timestamp)
        except KeyError:
            self.kv[key] = {
                'values': [value],
                'timestamp_list': [timestamp]
            }

    def get(self, key: str, timestamp: int) -> str:
        try:
            position = self.find_insertion_point(self.kv[key]['timestamp_list'], timestamp)
            if position == 0:
                return ""
            return self.kv[key]['values'][position - 1]
        except KeyError:
            return ""

    # binary search to reduce time
    def find_insertion_point(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) - 1
        while lower < upper:
            mid = math.floor((upper + lower + 1) / 2)
            if nums[mid] > target:
                upper = mid - 1
            elif nums[mid] <= target:
                lower = mid
        if lower == 0:
            if target < nums[0]:
                return 0
        return lower+1


if __name__ == '__main__':
    time_map = TimeMap()
    time_map.set("foo", "bar", 1)
    time_map.set("foo", "bar2", 4)
    time_map.set("foo", "bar3", 7)
    print(time_map.find_insertion_point([1, 4, 7], 1))
