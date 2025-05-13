"""
An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

"""
class Solution:
    def isUglyNumber(self,n : int)->bool:
        if n <= 0:
            return False
        for factor in [2,3,5]:
            while n % factor == 0:
                n //= factor
        return n == 1
s = Solution()
n = int(input("Enter the number : "))
print(s.isUglyNumber(n))