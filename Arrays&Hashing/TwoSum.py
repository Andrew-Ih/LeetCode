from typing import List

# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_map:
                return[prev_map[diff], i]
            prev_map[n] = i

# Time complexity: O(n^2)
# Space complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []

        for i in range(len(nums)):
            second_number = target - nums[i]
            if second_number in nums[i+1:]:
                return [i,nums.index(second_number, i + 1)]

        return result


