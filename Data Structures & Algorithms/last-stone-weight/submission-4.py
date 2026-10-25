class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) >= 2:
            stones.sort()
            one = stones.pop()
            two = stones.pop()
            if one != two:
                stones.append(max(one, two) - min(one, two))
        
        return stones[0] if stones else 0




