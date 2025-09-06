class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        for i in candies:
            cur = i + extraCandies
            check = False
            for j in candies:
                if j > cur:
                    check = True
            if check:
                result.append(False)
            else:  
                result.append(True)
        return result
        