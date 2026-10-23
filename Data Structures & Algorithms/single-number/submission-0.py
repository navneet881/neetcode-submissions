class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        for number in nums:
            seen[number] = seen.get(number, 0) + 1
        for key, count in seen.items():
            if count == 1: return key
