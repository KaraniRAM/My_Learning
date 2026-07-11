class Solution(object):
    def coinChange(self, coins, amount):
        """
    
        
        :type coins: List[int]
        :type amount: int
        :rtype: int"""
        n=amount 
        dp=[]
        for i in range(len(coins)):
            r=[]
            for j in range((n+1)):
                r.append(float('inf'))
            dp.append(r)
        for i in range(n+1):
                if i%coins[0]==0:
                    dp[0][i]=i//coins[0]
        for i in range(1,len(coins)):
            dp[i][0]=0
            for j in range(1,n+1):
             if j>=coins[i]:
                dp[i][j]=min(dp[i-1][j],1+dp[i][j-coins[i]])
             else:
                dp[i][j]=dp[i-1][j]
        return dp[len(coins)-1][n] if dp[len(coins)-1][n]!=float('inf') else -1
        #return dp
        
