class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2 = sorted(nums)
        i=0
        j=len(nums)-1
        res=[]
        while i<j:
            temp=nums2[i]+nums2[j]
            if temp==target:
                res.append(nums2[i])
                res.append(nums2[j])
                break
            elif temp>target:
                j-=1
            else:
                i+=1
        fr=[]
        for i in range(len(nums)):
            if nums[i]==res[0]:
                fr.append(i)
                nums[i]=sys.maxsize
            if nums[i]==res[1]:
                fr.append(i)  
                nums[i]=sys.maxsize
        fr.sort()
        return fr
