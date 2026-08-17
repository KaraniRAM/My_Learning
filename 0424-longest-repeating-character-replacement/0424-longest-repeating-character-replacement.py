class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        d={}
        i=0
        res=0
        for j in range(len(s)):
            d[s[j]]=d.get(s[j],0)+1
            maxfre=max(d.values())
            curr=j-i+1
            if curr-maxfre>k:
                d[s[i]]-=1
                i+=1
                curr=j-i+1
            res=max(res,curr)    
        return res        
        
        
        