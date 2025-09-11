class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        line1 = [1] * len(nums)
        line2= [1] * len(nums)
        for i in range(1,len(nums)):
            line1[i] = line1[i-1] * nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            line2[i] = line2[i+1] * nums[i+1]
        res= [1] * len(nums)
        for i in range(len(nums)):
            res[i] = line1[i] * line2[i]
        return res