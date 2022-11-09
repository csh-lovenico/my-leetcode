class Solution:
    def concatenatedBinary(self, n: int) -> int:
        bin_str = ''
        for i in range(1, n + 1):
            bin_str += bin(i)[2:]

        return int(bin_str, 2) % (10 ** 9 + 7)
