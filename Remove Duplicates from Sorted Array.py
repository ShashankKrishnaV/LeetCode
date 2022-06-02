class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index=0
        for run in range(1,len(nums)):
            if nums[run]!=nums[index]:
                index+=1
                nums[index]=nums[run]
        return index+1
