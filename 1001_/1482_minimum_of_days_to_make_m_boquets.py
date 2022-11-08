from typing import List


# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/discuss/2587672/Easy-to-read-python-binary-search-solution
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        # we will check for the minimal day able to grow all the flowers, to improve performance
        # we use binary search to check for the minimal day between min and max days.
        min_days = min(bloomDay)
        max_days = max(bloomDay)

        while min_days < max_days:
            mid = min_days + (max_days - min_days) // 2
            if self.check_the_day(day=mid, bloomDays=bloomDay, bouquets=m,
                                  flowers_per_bouquet=k):
                max_days = mid
            else:
                min_days = mid + 1

        return max_days

    def check_the_day(self, day: int, bloomDays: List[int], bouquets: int, flowers_per_bouquet: int) -> bool:
        """
        check in a linear way if the provided day can grow N bouquets with N adjacent flowers_per_bouquet each
        """
        bouquets_created = 0
        current_flowers = 0

        for bloomDay in bloomDays:
            if bloomDay > day:
                current_flowers = 0
            if bloomDay <= day:
                current_flowers += 1
            if current_flowers == flowers_per_bouquet:
                bouquets_created += 1
                current_flowers = 0

        return bouquets_created >= bouquets
