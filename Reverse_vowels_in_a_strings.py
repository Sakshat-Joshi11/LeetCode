"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.\

"""
class Solution:
    def reverse_vowels(self,s : str)->str:
        vowels = {'a','i','o','u','A','E','I','O','U'}
        char = list(s)
        left,right = 0,len(char)-1
        
        while left < right:
            while left < right and char[left] not in vowels:
                left +=1
            while left < right and char[right] not in vowels:
                right -=1
            char[left],char[right]=char[right],char[left]
            left +=1
            right-=1
        return ''.join(char)
t = Solution()
s = input("Enter the string : ")
print(t.reverse_vowels(s))