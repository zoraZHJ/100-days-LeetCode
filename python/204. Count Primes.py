class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * n
        isPrime[0] = False
        isPrime[1] = False

        count = 0

        for i in range(2, n):
            if isPrime[i]:
                for j in range(i * i, n, i):
                        isPrime[j] = False

        for i in range(n):
            if isPrime[i]:
                count += 1
        return count