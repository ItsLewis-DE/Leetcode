class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        max_can = candies[0]
        for i in candies:
            if max_can < i:
                max_can = i 
        for i in candies:
            cur = i + extraCandies
            if cur >= max_can:
                result.append(True)
            else:
                result.append(False)
        return result