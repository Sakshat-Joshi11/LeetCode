"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"

"""
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i,j = len(num1) - 1 ,len(num2) - 1
        carry = 0
        result = []
        while i >=0 or j >=0 or carry:
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0
            total = digit1 + digit2 + carry
            result.append(str(total%10))
            carry = total // 10
            i -= 1
            j -= 1
        return ''.join(result[::-1])
s = Solution()
print(s.addStrings(num1="456",num2="77"))