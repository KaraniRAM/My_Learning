class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        m=len(s[0])    
        w=[]   
        for i in s.split():
            w.append(i)
        g=len(w[-1])
        return g
        