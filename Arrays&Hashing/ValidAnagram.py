class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for letter in set(s):
            if s.count(letter) != t.count(letter):
                return False
        
        return True 
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        word1, word2 = {}, {}

        for letters in s:
            if letters in word1:
                word1[letters] += 1
            else:
                word1[letters] = 0

        for letters in t:
            if letters in word2:
                word2[letters] += 1
            else:
                word2[letters] = 0

        if word1 == word2:
            return True
        else:
            return False
        