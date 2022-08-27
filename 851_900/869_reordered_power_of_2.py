class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        pow_2_sort = set()
        for i in range(31):
            pow_2 = 2 ** i
            sorted_pow = ''.join(sorted(list(str(pow_2))))
            pow_2_sort.add(sorted_pow)

        return ''.join(sorted(list(str(n)))) in pow_2_sort
