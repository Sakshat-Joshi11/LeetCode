"""
Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

An alphanumeric string is a string consisting of lowercase English letters and digits.

 

Example 1:

Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
Example 2:

Input: s = "abc1111"
Output: -1
Explanation: The digits that appear in s are [1]. There is no second largest digit. 
 

Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters and digits.
 
"""
class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        Max,S_max = float("-inf"),float("-inf")
        for i in s:
            if i.isdigit():
                d = int(i)
                if d > Max:
                    S_max = Max
                    Max = d
                elif Max > d > S_max:
                    S_max = d
        return S_max if S_max != float("-inf") else -1
s = Solution()
print(s.secondHighest(s="dfa12321afd"))