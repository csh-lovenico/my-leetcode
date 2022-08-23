from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def binary_search(target: int) -> int:
            upper = len(arr) - 1
            lower = 0
            while lower < upper:
                mid = (lower + upper + 1) // 2
                if target < arr[mid]:
                    upper = mid - 1
                else:
                    lower = mid
            return lower

        pivot = binary_search(x)
        if pivot == 0 and arr[pivot] >= x:
            return arr[0:k]
        if pivot == len(arr) - 1:
            return arr[pivot - k + 1:]
        result = []
        l = pivot
        r = pivot + 1
        for i in range(k):
            if l < 0 and r < len(arr):
                result.append(arr[r])
                r += 1
                continue
            if r >= len(arr) and l >= 0:
                result.append(arr[l])
                l -= 1
                continue
            l_value = abs(arr[l] - x)
            r_value = abs(arr[r] - x)
            if l_value < r_value:
                result.append(arr[l])
                l -= 1
            elif l_value > r_value:
                result.append(arr[r])
                r += 1
            else:
                if arr[l] < arr[r]:
                    result.append(arr[l])
                    l -= 1
                else:
                    result.append(arr[r])
                    r += 1
        return sorted(result)


if __name__ == '__main__':
    print(Solution().findClosestElements([1, 5, 10], 1, 4))
