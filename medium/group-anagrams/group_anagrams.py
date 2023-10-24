class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        
        for word in strs:
            key = [0]*26
            
            for letter in word:
                index = ord(letter) - 97 # 97 is ASCII code of "a"
                key[index] += 1
                
            key = tuple(key)
            
            if key not in result:
                result[key] = [word]
            else:
                result[key].append(word)
                
        return result.values()