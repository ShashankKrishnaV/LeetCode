class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        c=-1
        for i in range(len(nums)):
            if nums[i]!=0:
                c+=1
                nums[i], nums[c] = nums[c], nums[i]
