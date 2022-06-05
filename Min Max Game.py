class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        b=False
        if len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return min(nums[0],nums[1])
        else:
            while len(nums)!=1:
                newNums=[]
                for i in range(0,len(nums)-1,2):
                    if b==False:
                        newNums.append(min(nums[i],nums[i+1]))
                        b=True
                    else:
                        newNums.append(max(nums[i],nums[i+1]))
                        b=False
                nums=newNums
            return nums[0]
