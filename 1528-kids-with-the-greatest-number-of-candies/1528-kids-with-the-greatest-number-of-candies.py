class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_can = max(candies)
        return [c + extraCandies>= max_can for c in candies]