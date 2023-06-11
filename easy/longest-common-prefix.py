class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        for letters in zip(*[s for s in strs]):
            if len(set(letters)) == 1:
                res.append(letters[0])
            else:
                return ''.join(res)
        return ''.join(res)