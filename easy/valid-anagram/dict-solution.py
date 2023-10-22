class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if self.count_letters(s) == self.count_letters(t):
            return True
        else:
            return False
        
        
    def count_letters(self, s: str) -> dict:
        letters = {}
        for letter in s:
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1
        
        return letters