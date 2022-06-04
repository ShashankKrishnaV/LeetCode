class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        psum=0
        minc=prices[0]
        diff=0
        for i in range(1,len(prices)):
            if prices[i]<prices[i-1]:
                minc=prices[i]
                psum+=diff
                diff=0
            elif prices[i]>prices[i-1]:
                temp=prices[i]-minc
                if temp>diff:
                    diff=temp
            if i==len(prices)-1 and diff!=0:
                psum+=diff
        return psum
