"""
Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.

 Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]

"""
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        full_set = set(range(1,len(nums)+1)) 
        missing_numbers = full_set - set(nums)
        return missing_numbers
s = Solution()
nums = list(map(int,input("Enter the numbers for the array : ").split(",")))
print(s.findDisappearedNumbers(nums))