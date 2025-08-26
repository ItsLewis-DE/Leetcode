class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i,val in enumerate(nums):
            if nums[abs(val)-1] <0:
                return abs(val)
            else:
                nums[abs(val)-1] = -nums[abs(val)-1]