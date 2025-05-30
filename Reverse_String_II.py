"""
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd
"""
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = []
        for i in range(0,len(s),2*k):
            result.append(s[i:i+k][::-1])
            result.append(s[i+k:i+2*k])
        return ''.join(result)
t = Solution()
s = input("Enter the string : ")
k = int(input("Enter the k : "))
print(t.reverseStr(s,k))