class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        trace = 1
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                trace+=1
        if trace==len(nums):
            nums.sort()
        else:
            index=-1
            ind_ele=0
            for i in range(len(nums)-1,0,-1):
                if nums[i]<=nums[i-1]:
                    continue
                else:
                    index=i-1
                    ind_ele=nums[index]
                    break
            index2 = -1
            ind2_ele = 0
            #print(ind_ele)
            for i in range(index+1,len(nums)):
                if nums[i]>nums[index]:
                    index2 = i
                    ind2_ele = nums[index2]
            nums[index], nums[index2] = nums[index2], nums[index]
            k=[]
            for i in range(index+1,len(nums)):
                k.append(nums[i])
            k.sort()
            j=0
            for i in range(index+1,len(nums)):
                nums[i] = k[j]
                j+=1
                
                    
                    
            
        
