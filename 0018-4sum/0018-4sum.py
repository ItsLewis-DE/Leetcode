class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result,res = [],[]
        nums.sort()
        def kSum(k,start,target):
            if k!=2:
                for i in range(start,len(nums)-k+1):
                    if i >start and nums[i] ==nums[i-1]:
                        continue
                    res.append(nums[i])
                    kSum(k-1,i+1,target -nums[i])
                    res.pop()
                return
            l,r = start,len(nums)-1
            while l<r:
                tong = nums[l] + nums[r]
                if tong < target:
                    l+=1
                elif tong > target:
                    r-=1
                else:
                    result.append(res + [nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        kSum(4,0,target)
        return result