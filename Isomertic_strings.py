"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_s_to_t = {}
        map_t_to_s = {}
        for char_s,char_t in zip(s,t):
            if char_s in map_s_to_t :
                if map_s_to_t[char_s] != char_t:
                    return False
            else:
                map_s_to_t[char_s] = char_t
            if char_t in map_t_to_s :
                if map_t_to_s[char_t] != char_s:    
                    return False 
            else:
                map_t_to_s[char_t] = char_s 
            
        return True
            
sol = Solution()
s = input("Enter the characters for s : ")
t = input("Enter the characters for t : ")
print(sol.isIsomorphic(s,t))