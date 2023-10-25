class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        freq = [[] for i in range(len(nums)+1)]
        
        for key, v in hashmap.items():
            freq[v].append(key)
            
        res = []
        
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
            if len(res) == k:
                return res
        