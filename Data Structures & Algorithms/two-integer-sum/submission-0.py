class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, number in enumerate(nums):
            dif = target - number
            if dif in seen:
                return [min(i, seen[dif]), max(i, seen[dif])]
            seen[number] = i
        return []
