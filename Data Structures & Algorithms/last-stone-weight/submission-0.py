class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        x,y = 0,0
        while len(stones) > 1:
            stones.sort()
            y, x = stones[-1], stones[-2]
            if x == y:
                stones.pop(-1)
                stones.pop(-1)
            elif x < y:
                stones[-1] = y-x
                stones.pop(-2)
        if len(stones) == 1:
            return sum(stones)
        else:
            return 0