class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows > len(s):
            return s
        result = [''] * numRows
        cur =0 
        goingDown = False
        for c in s:
            result[cur] += c
            if cur ==0 or cur == numRows -1:
                goingDown =  not goingDown
            cur += 1 if goingDown else -1
        return ''.join(result)