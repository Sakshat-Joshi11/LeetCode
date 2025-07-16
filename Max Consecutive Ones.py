"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2

"""
from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int: 
        count = 0
        Max_ones = 0
        for i in nums:
            if i == 1:
                count += 1
                Max_ones = max(Max_ones,count)
            if i == 0:
                count = 0
        return Max_ones
s = Solution()
print(s.findMaxConsecutiveOnes(nums=[1,1,0,1,1,1]))