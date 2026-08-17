class Solution(object):
    def maxProfit(self, prices):
        m=prices[0]
        maxi=0
        for i in range(len(prices)):
            m=min(m,prices[i])
            
            maxi=max(maxi,prices[i]-m)
        return maxi


            