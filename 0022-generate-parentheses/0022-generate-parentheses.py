class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        a=[]
        def para(s,op,cl):
            if len(s)==2*n:
                a.append(s)
                return 
            if op<n:
                para(s+"(",op+1,cl)
            if cl<op:
                para(s+")",op,cl+1)
        para("",0,0)
        return a
        