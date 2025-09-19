class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        khoang_cach = 1e9
        ket_qua = 0
        for i,a in enumerate(nums):
            l,r = i+1,len(nums)-1
            while l<r:
                tong = nums[l] + nums[r] + a
                if abs(tong- target) <khoang_cach:
                    khoang_cach = abs(tong-target)
                    ket_qua = tong
                if tong == target:
                    return target
                elif tong < target:
                    l+=1
                else:
                    r-=1
        return ket_qua