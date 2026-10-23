class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        number = next(i for i in range(len(nums) + 1) if i not in nums)
        return number