"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

 

Example 1:

Input: n = 27
Output: true
Explanation: 27 = 33
Example 2:

Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.
Example 3:

Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).

"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        while n % 3 == 0:
            n = n // 3
        return n == 1
s = Solution()
print(s.isPowerOfThree(n=27))