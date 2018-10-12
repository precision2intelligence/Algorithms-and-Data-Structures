#只考虑平方根
#过滤法，最快
'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        primes = [True for _ in range(n)]
        primes[0] = primes[1] = False
        for i in range(2,int(n**0.5)+1):
            if primes[i]:
                primes[i*i:n:i] = [False] * len(primes[i*i:n:i])
        return sum(primes)