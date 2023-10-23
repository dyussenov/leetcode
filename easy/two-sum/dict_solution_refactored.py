class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        candidates = {}
        for i, num in enumerate(nums):
            candidate = target-num
            if num in candidates:
                return [shifter, candidates[num]]     
            
            candidates[candidate] = num            
            shifter += 1