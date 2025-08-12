from typing import List

nums = [1, 2, 3, 1, 4, 5]

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for num in nums:
            if num in hash_map:
                print(f"Duplicate found: {num}")
                return True
            else:
                hash_map[num] = 0

        print("No duplicates found.")
        return False

solution = Solution()
result = solution.hasDuplicate(nums)
print(f"Result: {result}")