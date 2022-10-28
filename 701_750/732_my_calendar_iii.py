from sortedcontainers import SortedDict


# https://leetcode.com/problems/my-calendar-iii/discuss/2671881/Python-Simple-Python-Solution-Using-Sorted-Hashmap-or-Dictionary
class MyCalendarThree:

    def __init__(self):
        self.frequency = SortedDict()

    def book(self, start: int, end: int) -> int:

        current_value = 0
        result = 0

        if start not in self.frequency:
            self.frequency[start] = 1
        else:
            self.frequency[start] = self.frequency[start] + 1

        if end not in self.frequency:
            self.frequency[end] = -1
        else:
            self.frequency[end] = self.frequency[end] - 1

        for key in self.frequency:
            current_value = current_value + self.frequency[key]
            result = max(current_value, result)

        return result

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
