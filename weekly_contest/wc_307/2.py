from collections import defaultdict


class Solution:
    def largestPalindromic(self, num: str) -> str:
        result = ''
        num_dict = defaultdict(lambda: 0)
        for i in range(len(num)):
            num_dict[num[i]] += 1

        for i in range(9, -1, -1):
            if num_dict[str(i)] % 2 == 0:
                result += str(i) * (num_dict[str(i)] // 2)
                num_dict[str(i)] = 0
            elif num_dict[str(i)] >= 2:
                result += str(i) * (num_dict[str(i)] // 2)
                num_dict[str(i)] = 1

        use_single = False
        for i in range(9, -1, -1):
            if num_dict[str(i)] == 1:
                result += str(i)
                use_single = True
                break

        if not use_single:
            half = list(result)
            half.reverse()
            result = result + ''.join(half)
        else:
            half = list(result[:-1])
            half.reverse()
            result = result + ''.join(half)

        if result[0] == '0' and len(result) > 1:
            result = result.replace('0', '')

        if result == '':
            result = '0'
        return result


if __name__ == '__main__':
    print(Solution().largestPalindromic("00009"))
