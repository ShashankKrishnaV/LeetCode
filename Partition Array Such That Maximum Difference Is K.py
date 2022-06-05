class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        sublist=[]
        l=[]
        l.append(nums[0])
        sublist.append(l)
        ind=0
        for i in range(1,len(nums)):
            if (abs(nums[i]-sublist[ind][0]))<=k:
                sublist[ind].append(nums[i])

            else:
                l=[]
                l.append(nums[i])
                ind+=1
                sublist.append(l)
        print(sublist)
        return len(sublist)
