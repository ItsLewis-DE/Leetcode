class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dem =0
        left,right = 0,len(nums)-1
        nums.sort()
        while left < right:
            if nums[left] + nums[right] < k:
                left +=1
            elif nums[left] + nums[right] >k:
                right -=1
            else:
                dem+=1
                del nums[left]
                right -=1
                del nums[right]
                right -=1
        return dem
                