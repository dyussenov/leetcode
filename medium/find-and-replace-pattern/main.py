from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            word_hashmap = {}
            letters = set()
            for l1, l2 in zip(word, pattern):
                if l2 not in word_hashmap and l1 not in letters:
                    letters.add(l1)
                    word_hashmap[l2] = l1
                elif l2 in word_hashmap and l1 == word_hashmap[l2] and l1 in letters:
                    continue
                else:
                    break
            else:
                res.append(word)
        return res
