"""
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

 

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]

"""
from typing import List
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:
            if i % 2 == 0:
                result.insert(0,i)
            else:
                result.append(i)
        return result
s = Solution()
nums = list(map(int,input("Enter the array : ").split(",")))
print(s.sortArrayByParity(nums))