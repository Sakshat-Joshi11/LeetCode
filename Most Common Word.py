"""
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

Note that words can not contain punctuation symbols.

 

Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
Example 2:

Input: paragraph = "a.", banned = []
Output: "a"
 

Constraints:

1 <= paragraph.length <= 1000
paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
0 <= banned.length <= 100
1 <= banned[i].length <= 10
banned[i] consists of only lowercase English letters.

"""
import string
from typing import List
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for p in string.punctuation:
            paragraph = paragraph.replace(p," ")
        words = paragraph.lower().split()
        word_count = {}
        for word in words:
            if word not in banned:
                word_count[word] = word_count.get(word,0) + 1
        max_freq = float("-inf")
        max_word = ""
        for word,freq in word_count.items():
            if freq > max_freq:
                max_freq = freq
                max_word = word
        return max_word
s = Solution()
print(s.mostCommonWord(paragraph="Bob hit a ball, the hit BALL flew far after it was hit.",banned=["hit"]))