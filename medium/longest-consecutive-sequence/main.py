from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                current_longest = 0
                while num + current_longest in nums_set:
                    current_longest += 1
                longest = max(current_longest, longest)

        return longest


r = Solution()
case_1 = [100, 4, 200, 1, 3, 2]
case_2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(r.longestConsecutive(case_1))
