class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        candidates = {}
        shifter = 0
        
        for num in nums:
            candidate = target-num
            if num in candidates:
                return [shifter, candidates[num][1]]     
            
            candidates[candidate] = (num, shifter)            
            shifter += 1