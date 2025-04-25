class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        char_count = {}
        for char in nums:
            char_count[char] = char_count.get(char,0) + 1
            if char_count[char] > 1:
                return True
        return False      
s = Solution()
nums = list(map(int,input("Enter the value for the list seperated by commas : ").split(",")))
print(s.containsDuplicate(nums))