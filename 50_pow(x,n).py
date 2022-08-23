import math


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1 / x

        pow_l = [0.0] * (int(math.log2(abs(n))) + 1)
        pow_l[-1] = x
        result = 1
        bin_n = bin(abs(n))[2:]
        for i in range(len(pow_l) - 2, -1, -1):
            pow_l[i] = pow_l[i + 1] * pow_l[i + 1]

        for i in range(len(bin_n)):
            if bin_n[i] == '0':
                result *= 1
            else:
                result *= pow_l[i]

        if n > 0:
            return result
        else:
            return 1 / result


if __name__ == '__main__':
    print((Solution().myPow(2, -2)))
