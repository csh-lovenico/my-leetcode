# https://leetcode.com/problems/count-primes/discuss/2514873/Python-or-97-Fast-or-Sieve-of-Eratosthenes.
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = [0, 0] + [1] * (n - 2)
        i = 2
        while i * i < n:
            if primes[i]:
                primes[i * i:n:i] = [0] * ((n - i * i - 1) // i + 1)
            i += 1 if i == 2 else 2 # skip even numbers
        return sum(primes)
