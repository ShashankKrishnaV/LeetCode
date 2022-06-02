class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.append(-101)
        i=1
        while nums[i]!=-101:
            if nums[i]==nums[i-1]:
                nums.pop(i)
            else:
                i+=1
            
        return len(nums)-1
