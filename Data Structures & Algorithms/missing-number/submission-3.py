class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # return (len(nums) * (len(nums) + 1))//2 - sum(nums)
        normal = [i for i in range(len(nums) + 1)]
        return sum(normal) - sum(nums)

