"""
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

 

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

"""
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        rev_s = ""
        for char in s:
            if char.isalpha():
                rev_s = char + rev_s
        indices = []
        for i in range(len(s)):
            if not s[i].isalpha():
                indices.append((i,s[i]))
        for i,char in indices:
            rev_s = rev_s[:i]+char+rev_s[i:]
        return rev_s
t = Solution()
print(t.reverseOnlyLetters(s="Test1ng-Leet=code-Q!"))