class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low=99999
        diff=0
        for i in range(len(prices)):
            if prices[i]<low:
                low=prices[i]
            if i!=0 and prices[i]>prices[i-1]:
                temp=prices[i]-low
                if temp>diff:
                    diff=temp
        return diff
