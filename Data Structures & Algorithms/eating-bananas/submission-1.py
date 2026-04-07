class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minSpeed = 0
        left = 1
        right = max(piles) 
        while left <= right:
            k = (left + right) // 2
            total = 0
            for pile in piles:
                total += math.ceil(float(pile) / k)
            if total <= h:
                minSpeed = k
                right = k - 1 
            if total > h:
                left = k + 1
        return minSpeed 