"""
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
Example 2:

Input: arr = [1,1]
Output: 1

"""
from typing import List
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count_num = {}
        n = len(arr) // 4
        for i in arr:
            count_num[i] = count_num.get(i,0)+1
        for key,value in count_num.items():
            if value > n:
                return key
s = Solution()
arr = list(map(int,input("Enter the array seperated by commas : ").split(",")))
print(s.findSpecialInteger(arr))