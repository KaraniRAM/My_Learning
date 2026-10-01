class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        k=['(','[','{']
        d={']':'[','}':'{',')':'('}
        g=[]
        if s[0] not in k:
            return False
        if len(s)==1:
            return False
        for i in s:
            if i in k:
                g.append(i)
            else:
                if len(g)==0:
                    return False
                else:
                    if  g[-1]==d[i]:
                         g.pop()
                    else:
                        g.append(i)
        if len(g)==0:
            return True
        else:
            return False
        