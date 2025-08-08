"""
A sentence consists of lowercase letters ('a' to 'z'), digits ('0' to '9'), hyphens ('-'), punctuation marks ('!', '.', and ','), and spaces (' ') only. Each sentence can be broken down into one or more tokens separated by one or more spaces ' '.

A token is a valid word if all three of the following are true:

It only contains lowercase letters, hyphens, and/or punctuation (no digits).
There is at most one hyphen '-'. If present, it must be surrounded by lowercase characters ("a-b" is valid, but "-ab" and "ab-" are not valid).
There is at most one punctuation mark. If present, it must be at the end of the token ("ab,", "cd!", and "." are valid, but "a!b" and "c.," are not valid).
Examples of valid words include "a-b.", "afad", "ba-c", "a!", and "!".

Given a string sentence, return the number of valid words in sentence.

 

Example 1:

Input: sentence = "cat and  dog"
Output: 3
Explanation: The valid words in the sentence are "cat", "and", and "dog".
Example 2:

Input: sentence = "!this  1-s b8d!"
Output: 0
Explanation: There are no valid words in the sentence.
"!this" is invalid because it starts with a punctuation mark.
"1-s" and "b8d" are invalid because they contain digits.
Example 3:

Input: sentence = "alice and  bob are playing stone-game10"
Output: 5
Explanation: The valid words in the sentence are "alice", "and", "bob", "are", and "playing".
"stone-game10" is invalid because it contains digits.
 

Constraints:

1 <= sentence.length <= 1000
sentence only contains lowercase English letters, digits, ' ', '-', '!', '.', and ','.
There will be at least 1 token.

"""
class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split()
        count = 0
        for word in words:
            if self.isValid(word):
                count += 1
        return count
    def isValid(self,word:str)->bool:
            if any(ch.isdigit() for ch in word):
                return False
            if word.count("-") > 1:
                return False
            if "-" in word:
                idx = word.index("-")
                if idx == 0 or idx == len(word) -1:
                    return False
                if not (word[idx-1].isalpha() and word[idx+1].isalpha()):
                    return False
            if word and word[-1] in "!,.":
                word = word[:-1]
            return all(ch.isalpha() or ch =="-" for ch in word)
s = Solution()
print(s.countValidWords(sentence="alice and  bob are playing stone-game10"))